from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry("200x200")
def hellocallback():
    msg=messagebox.showinfo("click me","hello world")
b=Button(top,text="Click me",command=hellocallback)
b.place(x=20,y=50)
top.mainloop()

