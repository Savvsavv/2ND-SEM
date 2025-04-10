import tkinter as tk
from  tkinter import *

window = tk.Tk()
window.geometry("400x400")
window.title("ITCS103 TKINTER!")

label = tk.Label(window, text="USERNAME PLEASE")
label.pack()
entry= tk.Entry()
entry.pack()

window.mainloop()