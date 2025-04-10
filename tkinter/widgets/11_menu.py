import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITS103 TKINTER")

menu = tk.Menu(window)
window.config(menu=menu)# configure menu in window

filemenu =Menu(menu)# CREATED MENU FOR FILE
menu.add_cascade(label='File', menu=filemenu)# add ropdown
filemenu.add_command(label='New')#add commands or choices
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

window.mainloop()