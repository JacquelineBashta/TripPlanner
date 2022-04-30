from ast import Lambda
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

import json
import os.path

from RowEntry import RowEntry

##############################  Start of CLASS   ############################
class TripPlanner:
    
    def __init__(self,name):
        self.current_row = 0
        self.root = tk.Tk()
        self.root.title(name)
        self.root.option_add('*Font', "Candara")
        self.root.resizable(width=False, height=True) # disable width resize
        self.root.geometry('1600x700')
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

    ###################   Save/Load/Reload    ###################
    def Save_2_File(self):
               
        local_rows_dict ={}
        
        for row in self.all_rows_dict:
            local_row_dict = {}            
            for entry in self.all_rows_dict[row]:
                local_row_dict[entry]=self.all_rows_dict[row][entry].get()
                
            local_rows_dict[row]=local_row_dict
            
        self.Validate_Content()
        
        with open('trip.json', "w+") as fout:
            json.dump(local_rows_dict, fout)
        
    def Validate_Content(self):
        # Row Data
        #"From_Location","From_Date","From_Time"
        #"To_Location","To_Date","To_Time"
        #"By_MeansOfTransport","By_LinkForOffer","By_Cost")
        #"Stay_Where","Stay_LinkForOffer","Stay_Cost")
        #"Misc_Weather","Misc_Currency","Misc_MobileData")
        
        print("Validating...")
        previous_row = None
        current_row = None
        
        
        for row in self.all_rows_dict:
            current_row = RowEntry(self.all_rows_dict[row])
            
            # for each row validate entries not having default values
            
            if previous_row != None:
                #1) current entry to_location == previous entry from_location
                if current_row.From_Location != previous_row.To_Location:
                    
                    print("Error: current Location "+ current_row.From_Location + \
                        " and previous location "+ previous_row.To_Location + \
                            " doesn't match")
                    #if current entry date to_date > previous from_date
                        # check stay exist
                    
                    #else if current entry date == previous 
                        # check time difference > defined_time_frame (e.g. 2h)

                
                #2) change mean of transportation to dropdown -> default=None:
                      # based on the transportaion change the defined_time_frame
                
                #3) label summary to collect total time dates / days in each city / total cost
                
                #if self.all_rows_dict[current_row][self.entry_enum.From_Location].get() == \
                #        self.all_rows_dict[previous_row][self.entry_enum.From_Location].get():
                #    print("Error: "+self.all_rows_dict[current_row]["From_Location"].get())

            previous_row = RowEntry(self.all_rows_dict[row])

    def Load_From_File(self):
        row_count = 1
        local_rows_dict = {}
        with open("trip.json", "r+") as read_file:
            temp_rows_dict = json.load(read_file)
            # re-name the frame Ids as expected by tkinter
            for row in temp_rows_dict:
                if row_count == 1:
                    local_rows_dict["!frame"] =  temp_rows_dict[row]
                else:
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
        os.system('TripPlanner.py')

    def Delete_Row(self, widget:ttk.Button):
        self.all_rows_dict.pop(widget.master.winfo_name())
        widget.master.destroy()

##############################  End of CLASS   ############################

###################   MAIN    ###################        
def main():

    # Create object from the class Tripplanner
    trip = TripPlanner("Trip Planner App") 

    # Insert basic buttons
    trip.Add_Row_Button()
    trip.Save_Button()
    trip.Reload_Button()
        
    
    # if trip file exist, load from file
    if os.path.exists("trip.json"):
        trip.Load_From_File()
    else:
        #else create new trip        
        trip.Row_Entry()

    
    # Run forever!
    trip.root.mainloop()

if __name__ == '__main__':
    main()