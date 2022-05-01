from ast import Lambda
import logging
import tkinter as tk
from tkinter import ttk
import webbrowser
from tkcalendar import DateEntry

import json
import os.path

from RowEntry import RowEntry
from TP_FileHandler import TP_FileHandler
from ValidationLog import ValidationLog as VL

TRANSITION_TIME_DEFAULT = 15  #15 min
TRANSITION_TIME_FLIGHT = 2*60 #2 hours

Font_Small = ("Comic Sans MS", 8, "normal")
Font_Normal = ("Comic Sans MS", 10, "normal")
Font_Bold = ("Comic Sans MS", 10, "bold")

##############################  Start of CLASS   ############################
class TP_GUI:
    
    def __init__(self,name):
        self.current_row = 0
        self.root = tk.Tk()
        self.root.title(name)
        #self.root.resizable(width=False, height=True) # disable width resize
        self.root.geometry('1300x700')
        self.root.wm_attributes("-topmost", 1)
        self.register_validation = self.root.register(self.Validation)
        self.main_frame = self.Setup_Main_Frame()
        self.all_rows_dict = {}
        self.color = "lightgrey"

    def Setup_Main_Frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, fill=tk.BOTH)
        
        canvas=tk.Canvas( frame)
        canvas.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)
        
        vertibar=ttk.Scrollbar(frame, orient=tk.VERTICAL,command=canvas.yview)
        vertibar.pack(side=tk.RIGHT,fill=tk.Y)

        canvas.configure(yscrollcommand=vertibar.set)
        canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox('all')))

        main_frame = ttk.Frame(canvas)
        canvas.create_window((0,0), window=main_frame, anchor="nw")
        
        return main_frame

    def Validation(self,input):
        
        print("Validating...")

        self.Formate_Validate_Content()
        self.Logical_Validate_Content()
        
        print("Updating Summary...")

        self.Update_Summary()  
        
        print("^_^")
        
    ##############      File Menu     ########################
    def File_Menu(self):
        # Creating Menubar
        menubar = tk.Menu(self.root)
        
        # Adding File Menu and commands
        file = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='File', menu = file)
        file.add_command(label ='New Trip', command = None)
        file.add_command(label ='Open...', command = None)
        file.add_command(label ='Save', command =lambda: TP_FileHandler.Save_File(self.all_rows_dict))
        file.add_command(label ='Reload', command = self.Reload)
        file.add_separator()
        file.add_command(label ='Exit', command = self.root.destroy)

        # Add the menu bar to the top of the window
        self.root.config(menu=menubar)            
        
    ################      AddingFrames      ######################
    def Block_Entry(self,frame,row_dict, column_num:int, block_name:str, *entry_names ):
        pad = 5
        entry_count = len(entry_names)
        
        canvas = tk.Canvas(frame)
        canvas.configure(bd=3, relief="groove", highlightthickness=1)
        canvas.grid(row=self.current_row, column=column_num,padx=pad, pady=pad)
        
        label = ttk.Label(canvas, text=block_name , font=Font_Normal)
        label.grid(row=self.current_row,rowspan=entry_count, column=column_num,padx=pad, pady=pad)

        for entry_name in entry_names:
            
            if entry_name == "Date":
                entry = DateEntry(canvas,selectmode='day')
                
            elif entry_name == "Time":
                entry = ttk.Entry(canvas)
                entry.insert(0,"00:00")
                
            elif entry_name == "LinkForOffer":
                entry = tk.Entry(canvas, fg="blue", cursor="hand2")
                entry.insert(0,entry_name)
                entry.bind("<Button-1>", lambda event, a=entry: Open_Hyberlink(a) )
                
            else:
                entry = ttk.Entry(canvas)
                entry.insert(0,entry_name)
            
            entry.grid(row=self.current_row, column=column_num+1,padx=pad, pady=pad)
            entry.config(validate ="focusout", validatecommand =(self.register_validation, '%P'), font=Font_Small)
            
            row_dict[block_name+"_"+entry_name] = entry
            
            self.current_row +=1
            
        self.current_row= 0
    
    def Row_Entry_Options(self,frame,row_dict,column_num):
        pad = 5
        canvas = tk.Canvas(frame)
        canvas.configure(bd=3, relief="groove", highlightthickness=1)
        canvas.grid(row=self.current_row, column=column_num,padx=pad, pady=pad)
       
        button_save_note = ttk.Button(canvas, text="Notes")
        button_save_note.config(command=lambda: self.Open_Note_Window(button_save_note))
        button_save_note.pack()
        
        #Workaround to treat the Notes (get/delete) same as other Entries
        row_dict["Notes"] = tk.Entry()
        
        button_delete_row = ttk.Button(canvas, text="Delete Row")
        button_delete_row.config(command=lambda: self.Delete_Row(button_delete_row))
        button_delete_row.pack()
        
    def Row_Entry(self):
        # Toggle rows color for better ux
        if self.color == "lightgrey":
            self.color = "white"
        else:
            self.color = "lightgrey"
        
        #Start with creating a frame to hold row info
        frame = tk.Frame(self.main_frame)
        frame.configure(bg=self.color, bd=3, relief="groove", highlightthickness=2)
        frame.pack()

        row_dict = {}
        self.Block_Entry(frame,row_dict, 0,"From","Location","Date","Time")
        self.Block_Entry(frame,row_dict, 1,"To","Location","Date","Time")
        self.Block_Entry(frame,row_dict, 2,"By","MeansOfTransport","LinkForOffer","Cost")
        self.Block_Entry(frame,row_dict, 3,"Stay","Where","LinkForOffer","Cost")
        self.Block_Entry(frame,row_dict, 4,"Misc","Weather","Currency","MobileData")
        
        self.Row_Entry_Options(frame,row_dict, 5)
        
        self.all_rows_dict[frame.winfo_name()]= row_dict      

    def Add_Summary_Frame(self):
        frame_summary = tk.Frame(self.main_frame)
        frame_summary.configure(bg=self.color, bd=3, relief="groove", highlightthickness=2)
        frame_summary.pack()
        
        label_trip_duration = ttk.Label(frame_summary,text="Trip Duration: ",font=Font_Bold)
        self.label_trip_duration_value = ttk.Label(frame_summary,text="0",font=Font_Small)
        
        label_trip_in_glance = ttk.Label(frame_summary,text="Trip In Glance: ",font=Font_Bold)
        self.label_trip_in_glance_value = ttk.Label(frame_summary,text="0",font=Font_Small)

        label_trip_cost = ttk.Label(frame_summary,text="Trip Cost: ",font=Font_Bold)
        self.label_trip_cost_value = ttk.Label(frame_summary,text="0",font=Font_Small)
        
        label_trip_duration.grid(row=0, column=0,padx=5,pady=5)
        self.label_trip_duration_value.grid(row=1, column=0,padx=5,pady=5)
        
        label_trip_in_glance.grid(row=0, column=1,padx=5,pady=5)
        self.label_trip_in_glance_value.grid(row=1, column=1,padx=5,pady=5)
        
        label_trip_cost.grid(row=0, column=2,padx=5,pady=5)
        self.label_trip_cost_value.grid(row=1, column=2,padx=5,pady=5)
        
        
        #Add button
        button_add_row = ttk.Button(frame_summary, text="Add Row", command=self.Row_Entry)
        #button_add_row.place(relx =0.55,rely = 0)
        button_add_row.grid(row=2, column=0,columnspan=3,padx=5,pady=5)   
    
    def Open_Note_Window(self,widget:ttk.Button):
        newWindow = tk.Toplevel(self.root)
        newWindow.title("Note Window")
        newWindow.geometry("400x400")
        newWindow.wm_attributes("-topmost", 1)

        inputtxt = tk.Text(newWindow, height = 15, width = 35)
        inputtxt.pack()
        inputtxt.insert(1.0, self.all_rows_dict[widget.master.master.winfo_name()]["Notes"].get())
        
        # Button Creation
        note_save_button = ttk.Button(newWindow,text = "Save", \
                            command = lambda a=inputtxt, b=widget: self.Save_Note_Text(a,b))
        note_save_button.pack()

    
    def Formate_Validate_Content(self):
        pass
    
    def Update_Summary(self):

        total_cost = 0
        trip_in_glance = ""
        
        previous_row = None
        current_row = None
        
        # collect label_trip_duration_value
        first_row = RowEntry(list(self.all_rows_dict.values())[0])
        last_row = RowEntry(list(self.all_rows_dict.values())[-1])

        start_date = first_row.Get_From_DateTime()
        end_date = last_row.Get_To_DateTime()
        duration = (end_date - start_date).days


        for row in self.all_rows_dict:
            current_row = RowEntry(self.all_rows_dict[row])
            # collect label_trip_cost_value
            total_cost += current_row.Get_By_Cost()
            total_cost += current_row.Get_Stay_Cost()

            # collect label_trip_in_glance_value
            if previous_row != None:
                if current_row.Get_From_DateTime().date() > previous_row.Get_To_DateTime().date():
                    diff = current_row.Get_From_DateTime().date() - previous_row.Get_To_DateTime().date()
                    trip_in_glance += previous_row.To_Location +" for "+ str(diff.days) +" Days \n"
            
            previous_row = RowEntry(self.all_rows_dict[row])


        self.label_trip_cost_value.config(text = str(total_cost) +" €") 
        self.label_trip_duration_value.config(text = "Start: "+ str(start_date) + "\nEnd:   "+ str(end_date) + "\nDuration: " + str(duration) + " Days \n")
        self.label_trip_in_glance_value.config(text = trip_in_glance)
    
    def Logical_Validate_Content(self):
        previous_row = None
        current_row = None
        
        for row in self.all_rows_dict:
            current_row = RowEntry(self.all_rows_dict[row])
      
            # for each row validate entries not having default values
            
            if previous_row != None:
                # current entry to_location == previous entry from_location
                if current_row.From_Location != previous_row.To_Location:
                    
                    VL.validation_log("current Location "+ current_row.From_Location + \
                        " and previous location "+ previous_row.To_Location + \
                            " doesn't match")
                
                # check that  to_datetime > from_datetime of same entry
                if current_row.Get_To_DateTime() <= current_row.Get_From_DateTime():
                    VL.validation_log("Wrong timing for "+current_row.From_Location)  
                    
                #if current entry date from_date < previous to_date, check stay exist
                if current_row.Get_From_DateTime().date() < previous_row.Get_To_DateTime().date():
                    VL.validation_log("Added date " + current_row.From_Date+ " is in the past wrt "+ previous_row.To_Date)
                        
                elif current_row.Get_From_DateTime().date() > previous_row.Get_To_DateTime().date():
                    if previous_row.Stay_Where == "" or previous_row.Stay_Where == "Where" :
                        VL.validation_log("you should stay some where! , find a stay in "+previous_row.To_Location)
                    
                    #else if current entry date == previous 
                        # check time difference > defined_time_frame (e.g. 2h)
                else :
                    diff_minutes = ( current_row.Get_From_DateTime() - previous_row.Get_To_DateTime()).total_seconds()/ 60 

                    #based on the transportaion change the TRANSITION_TIME
                    if current_row.By_MeansOfTransport == "Flight":
                        transition_time = TRANSITION_TIME_FLIGHT
                    else: 
                        transition_time = TRANSITION_TIME_DEFAULT
                        
                    if diff_minutes <= transition_time :
                        VL.validation_log("Not enough time ("+str(int(diff_minutes/60))+" hours "+str(int(diff_minutes%60))+" minutes) for Transitions")

                
                #2) change mean of transportation to dropdown -> default=None:
                
                #3) label summary to collect total time dates / days in each city / total cost

            previous_row = RowEntry(self.all_rows_dict[row])
    
    
                
    def Reload(self):
        TP_FileHandler.Save_File(self.all_rows_dict)
        self.root.destroy()
        os.system('main.py')

    def Delete_Row(self, widget:ttk.Button):
        self.all_rows_dict.pop(widget.master.master.winfo_name())
        widget.master.master.destroy()

    def Save_Note_Text(self,inputtxt:tk.Text,frame_note_butt:ttk.Button):
        inp = inputtxt.get(1.0, "end-1c")
        Note_Entry = ttk.Entry()
        Note_Entry.insert(0,inp)
        self.all_rows_dict[frame_note_butt.master.master.winfo_name()]["Notes"] = Note_Entry
        TP_FileHandler.Save_File(self.all_rows_dict)

##############################  End of CLASS   ############################

def Open_Hyberlink(entry_link:tk.Entry):
    
    link_text = entry_link.get()
        
    if(link_text.startswith("http")):
        webbrowser.open_new(link_text)

