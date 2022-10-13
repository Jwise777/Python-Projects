import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(column=0, row=3, padx=(10,10) ,pady=(10,10))
        self.btncustom = Button(self.master, text="Submit Custom text", width=30, height=2, command=self.customHTML)
        self.btncustom.grid(column=1, row=3, padx=(10,10) , pady=(10,10))
        #Create an Entry Widget
        self.entry = Entry(self.master, width= 42)
        self.entry.grid(column=0, row=2, columnspan=3, padx=(10,10) , pady=(10,10))
        #label widget
        label= Label(self.master, text="Enter custom text, or click default HTML button", font=('Helvetica 13'))
        label.grid(column=0, row=0, padx=(10,10) , pady=(10,10))


      

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlText=entry.get()
        htmlFile=open("index.html", "w")
        htmlContent="<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
