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

def main():                     
    root = Tk()
    ww= Frame(root,background="red",padx=30,pady=30)
    ww.pack()
    e = Entry(ww)
    e.pack()

    reg = root.register(callback)
    
    e.config(validate ="focusout", 
            validatecommand =(reg, '%P'),invalidcommand=lambda: messagebox.showerror("Error", "you are stupid!, don't try again ever"))
    root.mainloop()

def time_test():
    from datetime import datetime
    val1=datetime.now()
    val2=datetime(year=2021,month=7,day=25,hour=11)
    val3=datetime(year=2021,month=7,day=25,hour=5)
    print(val1)
    print(val2)
    difference=val3-val2
    print("The time difference ",difference)


from tkinter import *
import webbrowser

def callback(text):
    print(text)
    #webbrowser.open_new(r"http://www.google.com")

root = Tk()
link = Entry(root, fg="blue", cursor="hand2")
link.insert(0,"Google Hyperlink")
link.pack()
link.bind("<Button-1>", lambda event, a=link.get(): callback(a) )

root.mainloop()