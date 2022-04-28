from multiprocessing.dummy import Array
import tkinter as tk

from tokenize import String
from turtle import bgcolor
from typing import List

import json
import os.path


class Tripplanner:
    
    def __init__(self,name):
        self.current_row = 0
        self.root = tk.Tk()
        self.root.title(name)
        self.root.option_add('*Font', "Candara")

        self.rows_array = []
        self.color = "lightgrey"

    def Block_Entry(self,frame,row_dict, column_num:int, block_name:String, *entry_names ):
        pad = 5
        entry_count = len(entry_names)
        
        label = tk.Label(frame, text=block_name)
        label.grid(row=self.current_row,rowspan=entry_count, column=column_num,padx=pad, pady=pad)

        for entry_name in entry_names:
            entry = tk.Entry(frame)
            entry.insert(0,entry_name)
            entry.grid(row=self.current_row, column=column_num+1,padx=pad, pady=pad)
            row_dict[block_name+"_"+entry_name] = entry
            
            self.current_row +=1
            
        self.current_row= 0
    
    def Row_Entry(self):
        if self.color == "lightgrey":
            self.color = "white"
        else:
            self.color = "lightgrey"
        
        frame = tk.Frame(self.root)
        frame.configure(bg=self.color,bd=50)
        frame.pack()
        
        row_dict = {}
    
        self.Block_Entry(frame,row_dict, 0,"From","Location","Date","Time")
        self.Block_Entry(frame,row_dict, 2,"To","Location","Date","Time")
        self.Block_Entry(frame,row_dict, 4,"By","MeansOfTransport","LinkForOffer","Price")
        self.Block_Entry(frame,row_dict, 6,"Stay","Where","LinkForOffer","Price")

        self.rows_array.append(row_dict)
    
    def Save_2_File(self):
        local_rows_array=[]
        for row in self.rows_array:
            local_row_dict = {}
            for entry in row:
                local_row_dict[entry]=row[entry].get()
            local_rows_array.append(local_row_dict)
        
        with open('trip.json', "w+") as fout:
            json.dump(local_rows_array, fout)
            
    def Load_From_File(self):
        with open("trip.json", "r+") as read_file:
            emps = json.load(read_file)
            for row in emps:
                self.Row_Entry()
                for key, value in row.items():
                    self.rows_array[-1][key].delete(0,'end')
                    self.rows_array[-1][key].insert(0,value)
                
    def Save_Button(self):
        button_save = tk.Button(self.root, text="Save", command=self.Save_2_File)
        button_save.place(relx =2,rely = 2,anchor = 'e')
        button_save.pack()

    def Create_Row_Button(self):
        button_create_row = tk.Button(self.root, text="Add Row", command=self.Row_Entry)
        button_create_row.pack()        

        
def main():
        
    #from tkinter import Tk, font
    #r = Tk() # you need a running tcl interpreter
    #print(font.families())

    trip = Tripplanner("Trip Planner App") 
    trip.Create_Row_Button()
    trip.Save_Button()
    
    #if trip file exist, load from file
    if os.path.exists("trip.json"):
        trip.Load_From_File()
    else:
        #else create new trip        
        trip.Row_Entry()

    
    # Run forever!
    trip.root.mainloop()

if __name__ == '__main__':
    main()