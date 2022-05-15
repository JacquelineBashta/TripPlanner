
from enum import Enum


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

    def save(self):
        """
        Save the email
        :param email:
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
            
        
    def add_row_entry_data(self):
        pass
    
    def delete_row_data(self,frame_name):
        return True
    
    def handle_widget_data(self): #Widget_Change
        pass
