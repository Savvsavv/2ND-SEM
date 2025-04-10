import tkinter as tk
from tkinter import *


window = tk.Tk()
window.geometry("300x300")
window.title("LOG IN ")

label = tk.Label(window, text="LOG IN")
label.pack(pady=10)

entry= tk.Entry()
entry.insert(0,"Username")
entry.pack()
entry2= tk.Entry()
entry2.insert(0,"Password")
entry2.pack(pady=10)

b1=tk.Button(window, text="Log In", bg="blue",fg="white", width=16)
b1.pack()

cb1=tk.Checkbutton(window, text="Remember Me?")
cb1.pack(side=LEFT)

label=tk.Label(window, text="Forgot Password?", fg="blue")
label.pack(side=RIGHT)

lb2=tk.Label(window, text= "Create an Account", fg="blue")
lb2.pack()

window.mainloop()
