###################   MAIN    ###################        
import os
from TripPlanner import TripPlanner


def main():

    # Create object from the class Tripplanner
    trip = TripPlanner("Trip Planner App") 

    trip.File_Menu()
    
    # Insert basic buttons
    trip.Add_Row_Button()
    
    # Insert summary frame
    trip.Add_Summary_Frame()
    
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