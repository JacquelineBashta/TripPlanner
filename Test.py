import tkinter
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
  
def callback(input):
      
    if input.isdigit():
        print(input)
        return True
                          
    elif input == "":
        print(input)
        return True
  
    else:
        print(input)
        return False
                          
root = Tk()
ww= Frame(root,background="red",padx=30,pady=30)
ww.pack()
e = Entry(ww)
e.pack()

reg = root.register(callback)
  
e.config(validate ="focusout", 
         validatecommand =(reg, '%P'),invalidcommand=lambda: messagebox.showerror("Error", "you are stupid!, don't try again ever"))
  
root.mainloop()