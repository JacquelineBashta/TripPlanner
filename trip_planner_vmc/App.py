
import tkinter as tk

from View import View
from Controller import Controller
from Model import Model


   
   
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Trip Planner App')
        self.geometry('1300x700')
        self.wm_attributes("-topmost", 1)

        # create a model
        model = Model('hello@pythontutorial.net')

        # create a view and place it on the root window
        view = View(self)
        #view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()