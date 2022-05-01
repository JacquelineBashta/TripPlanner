###################   MAIN    ###################        
import os
from TP_FileHandler import TP_FileHandler
from TP_GUI import TP_GUI


def main():

    # Create object from the class Tripplanner
    trip = TP_GUI("Trip Planner App")

    trip.File_Menu()
    
    # Insert summary frame
    trip.Add_Summary_Frame()
    
    # if trip file exist, load from file

    temp_rows_dict = TP_FileHandler.Load_File()
    if temp_rows_dict != {}:
        # re-name the frame Ids as expected by tkinter
        row_count = 2
        local_rows_dict = {}
        for row in temp_rows_dict:
            local_rows_dict["!frame"+str(row_count)] =  temp_rows_dict[row]
            row_count += 1
        for row in local_rows_dict:
            trip.Row_Entry()
            for key, value in local_rows_dict[row].items():
                trip.all_rows_dict[row][key].delete(0,'end')
                trip.all_rows_dict[row][key].insert(0,value)
    else:
        #else create new trip        
        trip.Row_Entry()
    
    # Run forever!
    trip.root.mainloop()

if __name__ == '__main__':
    main()