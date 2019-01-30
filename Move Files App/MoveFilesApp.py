# Author: Eric Muller
#
# Tested in Python 3.6.6
#
# This is an application that lets you select two directories and move files
# of a specific type from the first to the second. The bottom text box
# allows you to enter file type (include the .)
#
#
#
#

from tkinter import *
import tkinter as tk
import MoveFilesAppFunc

global folder_selected1
global folder_selected2


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(530,200)
        self.master.maxsize(530,200)
        self.master.title("Move Files")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clocks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: MoveFilesAppFunc.ask_quit(self))
        arg = self.master

        self.master = master
        self.master.geometry('{}x{}'.format(600, 200))
        self.master.title("Final Drill")
        self.master.config(bg='lightgray')

        self.btnBrowse1 = Button(self.master, text="Browse Source", width=12, height=1, command=lambda: MoveFilesAppFunc.BrowSrc(self))
        self.btnBrowse1.grid(row=0,column=1,padx=(20,0),pady=(40,10))

        self.btnBrowse2 = Button(self.master, text="Browse Dest.", width=12, height=1, command=lambda: MoveFilesAppFunc.BrowDir(self))
        self.btnBrowse2.grid(row=1,column=1,padx=(20,0),pady=(20,10))

        #this is our source text box. It gets autofilled with users chosen path
        self.txtBox1 = Entry(self.master, font=('Helvetica', 12), fg='black', bg='white', width=30)
        self.txtBox1.grid(row=0, column=2, padx=(20,0), pady=(30,0), columnspan=2)

        #this is the destination text box. It gets autofilled with users chosen path
        self.txtBox2 = Entry(self.master, font=('Helvetica', 12), fg='black', bg='white', width=30)
        self.txtBox2.grid(row=1, column=2, padx=(20,0), pady=(10,0), columnspan=2)

        #this is where the user enters what type of extension they want to move
        self.txtBox3 = Entry(self.master, font=('Helvetica', 12), fg='black', bg='white', width=10)
        self.txtBox3.grid(row=2, column=2, padx=(15,50), pady=(0,0))

        self.lblFileType = Label(self.master, text='File Type:', font=('Helvetica', 10), fg='black', bg='lightgray')
        self.lblFileType.grid(row=2, column=1, padx=(20, 0), pady=(0, 0))

        self.btnCheck = Button(self.master, text="Move Files", width=12, height=2, command=lambda: MoveFilesAppFunc.dirSwitch(self,self.txtBox1.get(),self.txtBox2.get()))
        self.btnCheck.grid(row=2,column=3,padx=(0,15),pady=(0,0))

        self.btnCheck = Button(self.master, text="?", width=1, height=1, command=lambda: MoveFilesAppFunc.QuestionMark(self))
        self.btnCheck.grid(row=0, column=4, padx=(50, 0), pady=(30, 0))
        


        

        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
