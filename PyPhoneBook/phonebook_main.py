# Python Ver:    3.6.6
#
#Author:   Eric Muller
#
#Tested OS: Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import phonebook_gui
import phonebook_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #height,width
        self.master.maxsize(500,300)
        #This CenterWindow method will center our app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clocks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a seperate a module,
        #keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
