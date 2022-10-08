import Tkinter

win = Tk()
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()

v.get()
'This is a test'
v.set("this is set by the program")
