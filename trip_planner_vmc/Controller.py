from enum import Enum

from ViewData import ViewData
from ModelData import ModelData

class ViewModelMap:
    def __init__(self, frame_name, view_data,model_data):
        self.frame_name = frame_name
        self.view_data = view_data
        self.model_data = model_data

class Action_E(Enum):
     Set = 1
     Get = 2
     Create = 3
     Update = 4
     Delete = 5

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view_model_map_arr = []

    def save(self):
        """
        Save the view_data into model_data
        :param :
        :return:
        """
        try:

            # save the model
            #self.model.email = email
            self.model.save()

            # show a success message

        except ValueError as error:
            # show an error message
            pass
            
        
    def add_row_entry_data(self,view_data:ViewData, frame_name):
        model_data = ModelData()
        self.view_model_map_arr.append(ViewModelMap(frame_name,view_data,model_data))
    
    def delete_row_data(self,frame_name):
        ret = False
        for map_object in self.view_model_map_arr:
            if frame_name == map_object.frame_name:
                self.view_model_map_arr.remove(map_object)
                ret = True

        return ret

    
    def handle_widget_data(self): #Widget_Change
        pass
