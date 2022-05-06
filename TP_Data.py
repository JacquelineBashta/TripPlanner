
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


from enum import Enum
from xmlrpc.client import boolean

from ValidationLog import ValidationLog as VL

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

    def Widget_Change(self,action:Action_E,frame_name,widget_name,widget_object):
        if action == Action_E.Create:
            if self.Is_Valid_Widget(widget_object) :
                if frame_name not in self.all_frames_dict.keys():
                    self.all_frames_dict[frame_name] = dict()
                self.all_frames_dict[frame_name][widget_name] = widget_object

        elif action == Action_E.Get:
            if frame_name in self.all_frames_dict.keys():
                if widget_name in self.all_frames_dict[frame_name].keys():
                    if self.Is_Valid_Widget(widget_object):
                        widget_object.delete(0,'end')
                        widget_object.insert(0,self.all_frames_dict[frame_name][widget_name])
                else:
                    VL.validation_log("Given Widget "+ widget_name +" doesn't exist!")
            else:
                VL.validation_log("Given Frame "+ frame_name +" doesn't exist!")
        else:
            VL.validation_log("Error, use Set or Get as parameter")
        pass
    
    def Frame_Change(self,action:Action_E,frame_name,,widget_object):