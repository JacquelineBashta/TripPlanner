from ast import Lambda
import logging
from textwrap import fill
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

import json
import os.path

from RowEntry import RowEntry
from ValidationLog import ValidationLog as VL

TRANSITION_TIME_DEFAULT = 15  #15 min
TRANSITION_TIME_FLIGHT = 2*60 #2 hours

##############################  Start of CLASS   ############################
class TripPlanner:
    
    def __init__(self,name):
        self.current_row = 0
        self.root = tk.Tk()
        self.root.title(name)
        self.root.resizable(width=False, height=True) # disable width resize
        self.root.geometry('1200x700')
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
        
    ##############      BUTTONS     ########################
    def Save_Button(self):
        button_save = ttk.Button(self.main_frame, text="Save", command=self.Save_2_File)
        #Dirty solution to place button side to side with "add Row2 botton, but it reply on the existance of the other button widget as pack"
        button_save.place(relx =0.65,rely = 0)
        #button_save.pack()

    def Add_Row_Button(self):
        button_add_row = ttk.Button(self.main_frame, text="Add Row", command=self.Row_Entry)
        #button_add_row.place(relx =0.55,rely = 0)
        button_add_row.pack()           

    def Reload_Button(self):
        button_reload = ttk.Button(self.main_frame, text="Reload", command=self.Reload)
        button_reload.place(relx =0.75,rely = 0)
        #button_reload.pack()      
        
    ################      AddingFrames      ######################
    def Block_Entry(self,frame,row_dict, column_num:int, block_name:str, *entry_names ):
        pad = 5
        entry_count = len(entry_names)
        
        label = ttk.Label(frame, text=block_name)
        label.grid(row=self.current_row,rowspan=entry_count, column=column_num,padx=pad, pady=pad)

        for entry_name in entry_names:
            
            if entry_name == "Date":
                entry = DateEntry(frame,selectmode='day')
                
            elif entry_name == "Time":
                entry = ttk.Entry(frame)
                entry.insert(0,"00:00")
                
            else:
                entry = ttk.Entry(frame)
                entry.insert(0,entry_name)
            
            entry.grid(row=self.current_row, column=column_num+1,padx=pad, pady=pad)
            entry.config(validate ="focusout", validatecommand =(self.register_validation, '%P'))
            
            row_dict[block_name+"_"+entry_name] = entry
            
            self.current_row +=1
            
        self.current_row= 0
    
    def Row_Entry(self):
        # Toggle rows color for better ux
        if self.color == "lightgrey":
            self.color = "white"
        else:
            self.color = "lightgrey"
        
        #Start with creating a frame to hold row info
        
        frame = tk.Frame(self.main_frame)
        frame.configure(bg=self.color, bd=3, relief="sunken", highlightthickness=2)
        frame.pack()

        
        row_dict = {}
        self.Block_Entry(frame,row_dict, 0,"From","Location","Date","Time")
        self.Block_Entry(frame,row_dict, 2,"To","Location","Date","Time")
        self.Block_Entry(frame,row_dict, 4,"By","MeansOfTransport","LinkForOffer","Cost")
        self.Block_Entry(frame,row_dict, 6,"Stay","Where","LinkForOffer","Cost")
        self.Block_Entry(frame,row_dict, 8,"Misc","Weather","Currency","MobileData")
        
        button_delete_row = ttk.Button(frame, text="Delete Row")
        button_delete_row.config(command=lambda: self.Delete_Row(button_delete_row))
        button_delete_row.grid(row=self.current_row,rowspan=3, column=10)
        
        self.all_rows_dict[frame.winfo_name()]= row_dict      

    def Add_Summary_Frame(self):
        frame_summary = tk.Frame(self.main_frame)
        frame_summary.configure(bg=self.color, bd=3, relief="sunken", highlightthickness=2)
        frame_summary.pack()
        
        label_trip_duration = ttk.Label(frame_summary,text="Trip Duration = ")
        self.label_trip_duration_value = ttk.Label(frame_summary,text="0")
        
        label_trip_in_glance = ttk.Label(frame_summary,text="Trip In Glance = ")
        self.label_trip_in_glance_value = ttk.Label(frame_summary,text="0")

        label_trip_cost = ttk.Label(frame_summary,text="Trip Cost = ")
        self.label_trip_cost_value = ttk.Label(frame_summary,text="0")
        
        label_trip_duration.grid(row=0, column=0)
        self.label_trip_duration_value.grid(row=0, column=1)
        
        label_trip_in_glance.grid(row=1, column=0)
        self.label_trip_in_glance_value.grid(row=1, column=1)
        
        label_trip_cost.grid(row=2, column=0)
        self.label_trip_cost_value.grid(row=2, column=1)
        
    ###################   Save/Load/Reload    ###################
    def Save_2_File(self):
               
        local_rows_dict ={}
        
        for row in self.all_rows_dict:
            local_row_dict = {}            
            for entry in self.all_rows_dict[row]:
                local_row_dict[entry]=self.all_rows_dict[row][entry].get()
                
            local_rows_dict[row]=local_row_dict
          
        with open('trip.json', "w+") as fout:
            json.dump(local_rows_dict, fout)
    
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
                #1) current entry to_location == previous entry from_location
                if current_row.From_Location != previous_row.To_Location:
                    
                    VL.validation_log("current Location "+ current_row.From_Location + \
                        " and previous location "+ previous_row.To_Location + \
                            " doesn't match")
                    
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
    
    def Load_From_File(self):
        row_count = 2
        local_rows_dict = {}
        with open("trip.json", "r+") as read_file:
            temp_rows_dict = json.load(read_file)
            # re-name the frame Ids as expected by tkinter
            for row in temp_rows_dict:
                local_rows_dict["!frame"+str(row_count)] =  temp_rows_dict[row]
                row_count += 1
            for row in local_rows_dict:
                self.Row_Entry()
                for key, value in local_rows_dict[row].items():
                    self.all_rows_dict[row][key].delete(0,'end')
                    self.all_rows_dict[row][key].insert(0,value)
                
    def Reload(self):
        self.Save_2_File()
        self.root.destroy()
        os.system('main.py')

    def Delete_Row(self, widget:ttk.Button):
        self.all_rows_dict.pop(widget.master.winfo_name())
        widget.master.destroy()

##############################  End of CLASS   ############################