import tkinter as tk
from tkinter import *

window =tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER")

scrollbar= tk.Scrollbar(window)
scrollbar.pack(side= RIGHT, fill=Y)
mylist= tk.Listbox(window, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, "this is line number" +str(line))

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

window.mainloop()