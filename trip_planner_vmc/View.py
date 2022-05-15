import re
import tkinter as tk
from tkinter import ttk
import webbrowser

from tkcalendar import DateEntry

from Controller import Action_E


Font_Small = ("Comic Sans MS", 8, "normal")
Font_Normal = ("Comic Sans MS", 10, "normal")
Font_Bold = ("Comic Sans MS", 10, "bold")
Row_Pad = 5

class ViewData:
    def __init__(self):
        # View Data
        self.From_Location       = None
        self.From_Date           = None
        self.From_Time           = None
        self.To_Location         = None
        self.To_Date             = None
        self.To_Time             = None
        self.By_MeansOfTransport = None
        self.By_LinkForOffer     = None
        self.By_Cost             = None
        self.Stay_Where          = None
        self.Stay_LinkForOffer   = None
        self.Stay_Cost           = None
        self.Misc_Weather        = None
        self.Misc_Currency       = None
        self.Misc_MobileData     = None
        self.Notes               = None
        
class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # create widgets
        self.main_frame = self.create_main_frame()
        self.file_menu = self.create_file_menu()
        self.summary_frame = self.create_summary_frame()
        
        # local variables
        self.window_color = "lightgrey"
        
        # set the controller
        self.controller = None
        
    ##############      Main Frame     ########################
    def create_main_frame(self):

        self.pack(expand=True, fill=tk.BOTH)
        
        canvas=tk.Canvas( self)
        canvas.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)
        
        vertibar=ttk.Scrollbar(self, orient=tk.VERTICAL,command=canvas.yview)
        vertibar.pack(side=tk.RIGHT,fill=tk.Y)

        canvas.configure(yscrollcommand=vertibar.set)
        canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox('all')))

        main_frame = ttk.Frame(canvas)
        canvas.create_window((0,0), window=main_frame, anchor="nw")
        
        return main_frame
    
    ##############      File Menu     ########################
    def create_file_menu(self):
        # Creating Menubar
        menubar = tk.Menu(self)
        
        # Adding File Menu and commands
        file = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='File', menu = file)
        file.add_command(label ='New Trip', command = None)
        file.add_command(label ='Open...', command = None)
        file.add_command(label ='Save', command =lambda: self.save_button_clicked)
        file.add_separator()
        file.add_command(label ='Exit', command = self.master.destroy)

        # Add the menu bar to the top of the window
        self.master.config(menu=menubar)

    ##############      Summary Frame     ########################
    def create_summary_frame(self):
        frame_summary = tk.Frame(self.main_frame)
        #TODO : add color bg=self.window_color,
        frame_summary.configure( bd=3, relief="groove", highlightthickness=2)
        frame_summary.pack()
        
        label_trip_duration = ttk.Label(frame_summary,text="Trip Duration: ",font=Font_Bold)
        self.label_trip_duration_value = ttk.Label(frame_summary,text="0",font=Font_Small)
        
        label_trip_in_glance = ttk.Label(frame_summary,text="Trip In Glance: ",font=Font_Bold)
        self.label_trip_in_glance_value = ttk.Label(frame_summary,text="0",font=Font_Small)

        label_trip_cost = ttk.Label(frame_summary,text="Trip Cost: ",font=Font_Bold)
        self.label_trip_cost_value = ttk.Label(frame_summary,text="0",font=Font_Small)
        
        label_trip_duration.grid(row=0, column=0,padx=5,pady=5)
        self.label_trip_duration_value.grid(row=1, column=0,padx=5,pady=5)
        
        label_trip_in_glance.grid(row=0, column=1,padx=5,pady=5)
        self.label_trip_in_glance_value.grid(row=1, column=1,padx=5,pady=5)
        
        label_trip_cost.grid(row=0, column=2,padx=5,pady=5)
        self.label_trip_cost_value.grid(row=1, column=2,padx=5,pady=5)
        
        
        #Add button
        button_add_row = ttk.Button(frame_summary, text="Add Row", command=self.add_row_entry)
        #button_add_row.place(relx =0.55,rely = 0)
        button_add_row.grid(row=2, column=0,columnspan=3,padx=5,pady=5)   
    ##############      Note Window     ########################    
    def open_note_window(self,widget:ttk.Button):
        newWindow = tk.Toplevel(self.master)
        newWindow.title("Note Window")
        newWindow.geometry("400x400")
        newWindow.wm_attributes("-topmost", 1)

        inputtxt = tk.Text(newWindow, height = 15, width = 35)
        inputtxt.pack()

        #Get the Note info from dict to the gui
        note_entry_text = self.handle_widget(Action_E.Get, widget.master.master.winfo_name(), "Notes")
        #note_text = note_entry.get()
        inputtxt.insert(1.0, note_entry_text)
        
        # Button Creation
        note_save_button = ttk.Button(newWindow,text = "Save", \
                            command = lambda a=inputtxt, b=widget: self.save_note_text(a,b))
        note_save_button.pack()   
    
    def save_note_text(self,inputtxt:tk.Text,frame_note_butt:ttk.Button):
        
        note_text = inputtxt.get(1.0, "end-1c")
        self.handle_widget(Action_E.Set, frame_note_butt.master.master.winfo_name(), "Notes", widget_value = note_text)
        
        self.save_button_clicked()
        
    ##############      Others     ########################     
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def handle_widget(self,action:Action_E,frame_name,widget_name,widget_object=None,widget_value=None):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.handle_widget_data()
        return "Joka"
          
    def add_row_entry(self):
        """
        Handle button click event
        :return:
        """
        # Toggle rows color for better ux
        if self.window_color == "lightgrey":
            self.window_color = "white"
        else:
            self.window_color = "lightgrey"
        
        #Start with creating a frame to hold row info
        frame = tk.Frame(self.main_frame)
        frame.configure(bg=self.window_color, bd=3, relief="groove", highlightthickness=2)
        frame.pack()
        
        view_data = ViewData()

        self.create_block(view_data, frame, 0,"From","Location","Date","Time")
        self.create_block(view_data, frame, 1,"To","Location","Date","Time")
        self.create_block(view_data, frame, 2,"By","MeansOfTransport","LinkForOffer","Cost")
        self.create_block(view_data, frame, 3,"Stay","Where","LinkForOffer","Cost")
        self.create_block(view_data, frame, 4,"Misc","Weather","Currency","MobileData")
        
        self.create_row_options( view_data,frame, 5)
        
        if self.controller:
            self.controller.add_row_entry_data()
    
    def delete_row_entry(self, widget:ttk.Button):
        """
        delete the how row entry from view and database
        :return: 
        """
        if self.controller:
            if self.controller.delete_row_data(widget.master.master.winfo_name()) == True:
                widget.master.master.destroy()
        
    def create_block(self,view_data, frame, column_num:int, block_name:str, *entry_names):
 
        current_grid_row = 0
        entry_count = len(entry_names)
        
        canvas = tk.Canvas(frame)
        canvas.configure(bd=3, relief="groove", highlightthickness=1)
        canvas.grid(row=current_grid_row, column=column_num,padx=Row_Pad, pady=Row_Pad)
        
        label = ttk.Label(canvas, text=block_name , font=Font_Normal)
        label.grid(row=current_grid_row,rowspan=entry_count, column=column_num,padx=Row_Pad, pady=Row_Pad)

        for entry_name in entry_names:
            #Create individual Entry objects
            if entry_name == "Date":
                entry = DateEntry(canvas,selectmode='day')
                
            elif entry_name == "Time":
                entry = ttk.Entry(canvas)
                entry.insert(0,"00:00")
                
            elif entry_name == "LinkForOffer":
                entry = tk.Entry(canvas, fg="blue", cursor="hand2")
                entry.insert(0,entry_name)
                entry.bind("<Button-1>", lambda event, a=entry: self.open_hyberlink(a) )
                
            else:
                entry = ttk.Entry(canvas)
                entry.insert(0,entry_name)
            
            entry.grid(row=current_grid_row, column=column_num+1,padx=Row_Pad, pady=Row_Pad)
            #entry.config(validate ="focusout", validatecommand =(self.register_validation, '%P'), font=Font_Small)

            frame_name = frame.winfo_name()
            widget_name = block_name+"_"+ entry_name

            view_data.widget_name = entry
            #self.tp_data_obj.Widget_Change(Action_E.Create, frame_name, widget_name, widget_object = entry)
            
            current_grid_row +=1
        
        
    def create_row_options(self, view_data, frame, column_num):
        canvas = tk.Canvas(frame)
        canvas.configure(bd=3, relief="groove", highlightthickness=1)
        canvas.grid(row=0, column=column_num,padx=Row_Pad, pady=Row_Pad)
       
        button_row_notes = ttk.Button(canvas, text="Notes")
        button_row_notes.config(command=lambda: self.open_note_window(button_row_notes))
        button_row_notes.pack()
        
        view_data.Notes = tk.Entry()
        #self.tp_data_obj.Widget_Change(Action_E.Create, frame.winfo_name(), "Notes", widget_object= tk.Entry())
        
        button_delete_row = ttk.Button(canvas, text="Delete Row")
        button_delete_row.config(command=lambda: self.delete_row_entry(button_delete_row))
        button_delete_row.pack()
            
    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save()
 
        
    def open_hyberlink(entry_link:tk.Entry):
        
        link_text = entry_link.get()
            
        if(link_text.startswith("http")):
            webbrowser.open_new(link_text)
            
        