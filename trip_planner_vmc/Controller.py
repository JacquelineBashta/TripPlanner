from enum import Enum
from webbrowser import get

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

    def save_all_view(self):
        """
        Save the view_data into model_data
        :param :
        :return:
        """
        try:
            for map_object in self.view_model_map_arr:
                    values = map_object.view_data.get_view_data_values()
                    print("Debug ---> " +  str(values) )
                    map_object.model_data.set_model_data(values)

            # save the model to file
            self.model.save_all_model()

            # show a success message

        except ValueError as error:
            # show an error message
            pass

    def add_row_data(self,view_data:ViewData, frame_name):
        model_data = ModelData()
        self.view_model_map_arr.append(ViewModelMap(frame_name,view_data,model_data))

    def delete_row_data(self,frame_name):
        ret = False
        for map_object in self.view_model_map_arr:
            if frame_name == map_object.frame_name:
                self.view_model_map_arr.remove(map_object)
                ret = True

        return ret

    def handle_widget_data(self,action:Action_E, frame_name, widget_name, widget_value=None) -> str:
        val = ""
        for map_object in self.view_model_map_arr:
            if frame_name == map_object.frame_name:
                if action == Action_E.Set:
                    map_object.view_data.set_view_data_value(widget_name,widget_value)
                elif action == Action_E.Get:
                    val = map_object.view_data.get_view_data_value(widget_name)
                    print(val)

        return val
