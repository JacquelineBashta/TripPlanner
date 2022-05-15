
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


from enum import Enum
from xmlrpc.client import boolean

from validation_log import ValidationLog as VL

class Action_E(Enum):
     Set = 1
     Get = 2
     Create = 3
     Update = 4
     Delete = 5

class TP_Data:
    def __init__(self):
        self.all_frames_dict=dict()
        pass

    def Is_Valid_Widget(self,widget_object)-> boolean :
        if ((type(widget_object) is tk.Entry) or (type(widget_object) is ttk.Entry) or(type(widget_object) is DateEntry)):
            return True
        else:
            VL.validation_log("Only Widget of type \"Entry\" is supported")
            print(type(widget_object))
            return False

    def Widget_Change(self,action:Action_E,frame_name,widget_name,widget_object=None,widget_value=None):
        if action == Action_E.Create:
            if self.Is_Valid_Widget(widget_object) :
                if frame_name not in self.all_frames_dict.keys():
                    self.all_frames_dict[frame_name] = dict()
                self.all_frames_dict[frame_name][widget_name] = widget_object

        elif action == Action_E.Get:
            if frame_name in self.all_frames_dict.keys():
                if widget_name in self.all_frames_dict[frame_name].keys():
                    return self.all_frames_dict[frame_name][widget_name].get()
                else:
                    VL.validation_log("Given Widget "+ widget_name +" doesn't exist!")
            else:
                VL.validation_log("Given Frame "+ frame_name +" doesn't exist!")
                
        elif action == Action_E.Set:
            if frame_name in self.all_frames_dict.keys():
                if widget_name in self.all_frames_dict[frame_name].keys():
                    self.all_frames_dict[frame_name][widget_name].delete(0,'end')
                    self.all_frames_dict[frame_name][widget_name].insert(0, widget_value)
                else:
                    VL.validation_log("Given Widget "+ widget_name +" doesn't exist!")
            else:
                VL.validation_log("Given Frame "+ frame_name +" doesn't exist!")
                        
        else:
            VL.validation_log("Error, use Create, Set or Get as parameter")
        pass
    
    def Frame_Change(self,action:Action_E,frame_name,frame_dict_obj):
        if action == Action_E.Set:
            for key, value in frame_dict_obj.items():
                
                if self.Is_Valid_Widget( self.all_frames_dict[frame_name][key]) :
                    self.all_frames_dict[frame_name][key].delete(0,'end')
                    self.all_frames_dict[frame_name][key].insert(0,value)
        