import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("200x200")
window.title("ITCS103 TKINTER")

#THIS IS TO HOLD THE CHOSEN BOXES
gender= IntVar

#this is the checkboxes itself
rb1= tk.Radiobutton(window, text ="male", variable=gender, value="male")
rb2= tk.Radiobutton(window, text ="female", variable=gender, value="female")
rb1.pack()
rb2.pack()

window.mainloop()