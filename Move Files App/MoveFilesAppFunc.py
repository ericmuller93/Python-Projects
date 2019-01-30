import tkinter
from tkinter import *
from tkinter import filedialog
import os
import sqlite3
import MoveFilesApp
from tkinter import messagebox
import os
import shutil


def BrowSrc(self): #searches a folder and places path into txtbox1
    folder_selected1 = filedialog.askdirectory()
    self.txtBox1.insert(INSERT, folder_selected1)

def BrowDir(self): #searches a folder and places path into txtbox2
    folder_selected2 = filedialog.askdirectory()
    self.txtBox2.insert(INSERT, folder_selected2)

def ask_quit(self):
    if messagebox.askokcancel("Exit Progress", "Okay to exit application?"):
        #this closes the app
        self.master.destroy()
        os._exit(0)

def dirSwitch(self,folder_selected1,folder_selected2):
    myPath = (folder_selected1)
    listDir = os.listdir(myPath)
    fileType = self.txtBox3.get()
    i = 0
    while i < len(listDir):
    #isolate extention
        splitPath = os.path.splitext(listDir[i])
        #does it end in .txt
        if splitPath[1] == fileType:
        #if .txt concat path and time
            sourceFolder = (os.path.join(myPath,listDir[i]))
            timeEdited = os.path.getmtime(sourceFolder)
            print(listDir[i],timeEdited)
            shutil.move(sourceFolder, folder_selected2)
        # now this will create a database for these file names
            conn = sqlite3.connect('FilesMoved.db')
            with conn:
                cur = conn.cursor()  # create the table if it hasnt been created
                cur.execute("CREATE TABLE if not exists tbl_FilesMoved( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_FileName TEXT, \
                    col_LastTimeEdited TEXT \
                    );")
                conn.commit()
                cur.execute("""INSERT INTO tbl_FilesMoved (col_FileName,col_LastTimeEdited) VALUES (?,?)""",(listDir[i],timeEdited))
                conn.commit()
            conn.close()
        i += 1

def QuestionMark(self):
    messagebox.showinfo("Help Icon","Hi! This is an application that lets you select two directories and move files of a specific extension from the first to the second. The bottom text box allows you to enter file type (include the .) ")



if __name__ == "__main__":
    pass
