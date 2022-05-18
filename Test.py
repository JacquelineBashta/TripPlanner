from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import this
#print(dir("tkinter"))
  
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

def weblink():
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
    
# creates a Tk() object
master = Tk()
 
# sets the geometry of main
# root window
master.geometry("200x200")
 
 
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    # TextBox Creation
    inputtxt = Text(newWindow,
                    height = 5,
                    width = 20)
    inputtxt.insert(END, '"NEW WINDOW TEXT"\n')
    
    inputtxt.pack()
    
    # Label Creation
    lbl = Label(newWindow, text = "")
    lbl.pack()
    
    # Button Creation
    printButton = Button(newWindow,
                            text = "Print", 
                            command = lambda a=inputtxt,b=lbl: printInput(a,b))
    printButton.pack()
    

 
def printInput(text_widget:Text,lbl:Label):
    inp = text_widget.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
    
     
label = Label(master,
              text ="This is the main window")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btn = Button(master,
             text ="Click to open a new window",
             command = openNewWindow)
btn.pack(pady = 10)
 
# mainloop, runs infinitely
mainloop()