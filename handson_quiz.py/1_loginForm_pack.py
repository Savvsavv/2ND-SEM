import tkinter as tk
from tkinter import *


window = tk.Tk()
window.geometry("300x300")
window.title("LOG IN ")

#frame
frame=tk.Frame()
s_frame=tk.Frame()

#log in
label = tk.Label(frame, text="LOG IN", font=("Arial",10))
label.pack(pady=10)

#entry
entry= tk.Entry(frame)
entry.insert(0,"Username")
entry.pack()
entry2= tk.Entry(frame)
entry2.insert( 0,"Password")
entry2.pack(pady=10)

b1=tk.Button(frame, text="Log In", bg="blue",fg="white", width=16, font=("Arial",10))
b1.pack()

cb=tk.IntVar()
cb=tk.Checkbutton(frame, text="Remember Me?", font=("Arial",7), variable=cb)
cb.pack(side=LEFT,pady=2)

label=tk.Label(frame, text="Forgot Password?", fg="blue", font=("Arial",7))
label.pack(side=RIGHT, pady=2)

canvas = tk.Canvas(s_frame, width=40, height=10)
canvas.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
canvas.create_line(0, y, canvas_width, y)

lb2=tk.Label(s_frame, text= "Create an Account", fg="blue", font=("Arial",7))
lb2.pack(pady=2)

frame.pack()
s_frame.pack()
window.mainloop()
