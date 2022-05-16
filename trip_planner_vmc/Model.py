from collections import namedtuple
import re
import json
import os

from ModelData import ModelData

file_name = './Trips/trip_Tests_2.json'

class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save_all_model(self,model_data_arr):
        """
        Save the email into a file
        :return:
        """
        print("Saving...")
        model_data_dict_arr = []
        for model_data_object in model_data_arr:
            model_data_dict_arr.append(vars(model_data_object))
        with open(file_name, "w+") as fout:
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

        if os.path.exists(file_name):
            with open(file_name, "r+") as read_file:
                model_data_json_arr = json.load(read_file)
        
        for obj in model_data_json_arr:
            model_data_obj = ModelData()

            model_data_obj.set_all_model_data(list(obj.values()))
            model_data_objs_arr.append(model_data_obj)
        
        print("Loaded")

        return model_data_json_arr
        

