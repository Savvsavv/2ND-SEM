import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("Place Method Tutorial")

#button widget
b2= tk.Button(window, text="PACK BUTTON")
b2.pack(fill = X, expand =True, ipady =10)

#button widget
b1= tk.Button(window, text = "PLACE BUTTON")

#this is where b1 is plced inside b2 with in_option
b1.place(in_=b2, relxx = 0.5, rely=0.5, anchor = CENTER)

window.mainloop()