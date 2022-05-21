import json
import os

from utils.ModelData import ModelData

class Model:
    def __init__(self, name):
        self.file_name = './Trips/trip_Tests_2.json'

    def save_all_model(self,model_data_arr):
        """
        Save the email into a file
        :return:
        """
        print("Saving...")
        model_data_dict_arr = []
        for model_data_object in model_data_arr:
            model_data_dict_arr.append(vars(model_data_object))
        with open(self.file_name, "w+") as fout:
            json.dump(model_data_dict_arr, fout)
        print("Saved")


    def load_all_model(self):
        """
        Save the email into a file
        :return:
        """
        print("Loading...")

        model_data_json_arr = []  
        model_data_objs_arr = []  

        if os.path.exists(self.file_name):
            with open(self.file_name, "r+") as read_file:
                model_data_json_arr = json.load(read_file)
        
        for obj in model_data_json_arr:
            model_data_obj = ModelData()

            model_data_obj.set_all_model_data(list(obj.values()))
            model_data_objs_arr.append(model_data_obj)
        
        print("Loaded")

        return model_data_objs_arr
        

