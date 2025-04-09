import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("Pack Method Tutorial")

#Create a frame that expands according to window size
pane = tk.Frame(window)
pane.pack(fill = BOTH, expand= True)

#button widgets which can also expand and fill
b1= tk.Button(pane,tex ="Click Me!")
b1.pack(fill = BOTH, expand = True)

b2= tk.Button(pane,tex ="Click Me 2!")
b2.pack(fill = BOTH, expand = True)

window.mainloop()