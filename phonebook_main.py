# Python ver: 3.7.1
#
# Author: James Wise
# 
# Purpose: Phonebook Demo, OOP, Tkinter GUI Module
#

from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# So we can have access to them

import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        # define our master frame configuartion
        self.master = master
        self.master.minsize(500,300) #(hght,wdth)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch if
        #The user clicks on the upper corner, "x" in windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a seperate module,
        # Keeping your code clutter free
        phonebook_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
