import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("500x500")
window.title("ITCS103 TKINTER")

#this is to hod the chosen boxes
var1= IntVar()
var2= IntVar()

#this it the checkboxes itself
cb1= tk.Checkbutton(window,text="Table Tennis", variable=var1)#variable is used to push the data to the IntVar()
cb2= tk.Checkbutton(window,text="Chess", variable=var2)#variable is used to push the data to the IntVar()
cb1.pack()
cb2.pack()

window.mainloop()