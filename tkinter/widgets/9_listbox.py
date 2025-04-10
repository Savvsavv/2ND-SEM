import tkinter as tk
from tkinter import *

window= tk.Tk()
window.geometry("330x330")
window.title("ITCS103 TKINTER")

listbox= tk.Listbox(window)#main panel for list box
listbox.insert(1, "PYTHON")#ADD TEMS IN LIST BOX
listbox.insert(2, "C##")#ADD TEMS IN LIST BOX
listbox.insert(3, "JAVA")#ADD TEMS IN LIST BOX
listbox.insert(4, "PERL")

listbox.pack()

window.mainloop()