
from webbrowser import get

from utils.Action_E import Action_E
from utils.ViewData import ViewData
from utils.ModelData import ModelData
from utils.ViewModelMap import ViewModelMap


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
            model_data_arr = []
            for map_object in self.view_model_map_arr:
                    values = map_object.view_data.get_all_view_data_value()
                    map_object.model_data.set_all_model_data(values)
                    model_data_arr.append(map_object.model_data)

            # save the model to file
            self.model.save_all_model(model_data_arr)

            # show a success message

        except ValueError as error:
            # show an error message
            pass

    def load_all_view(self):
        model_data_objs_arr = self.model.load_all_model()


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

        return val
