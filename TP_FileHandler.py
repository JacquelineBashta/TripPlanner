import json
import os


class TP_FileHandler:
    def __init__(self):  
        pass
###################   Save/Load/Reload    ###################
    def Save_File(all_rows_dict):
        print("Saving...")
        local_rows_dict ={}
        
        for row in all_rows_dict:
            local_row_dict = {}            
            for entry in all_rows_dict[row]:
                local_row_dict[entry]=all_rows_dict[row][entry].get()
                
            local_rows_dict[row]=local_row_dict
        
        with open('trip.json', "w+") as fout:
            json.dump(local_rows_dict, fout)
        
        print("Saved")

    def Load_File():
        temp_rows_dict ={}
        if os.path.exists("trip.json"):
            with open("trip.json", "r+") as read_file:
                temp_rows_dict = json.load(read_file)
        return temp_rows_dict