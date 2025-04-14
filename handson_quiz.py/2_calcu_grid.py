import tkinter as tk
from tkinter import *

window=tk.Tk()
window.geometry("440x500")
window.title("Calculator")

#frame
frame=tk.Frame()
s_frame=tk.Frame()

#Entries
entry=tk.Entry(frame, width=10, justify="right")
ans=tk.Entry(frame,width=13, justify="right")

#grid
entry.grid(row=0,column=0,pady=3,padx=3,sticky="news")
ans.grid(row=1,column=0,pady=3,padx=3,sticky="news")


#1st row
nine= tk.Button(s_frame, text="9", width=5, height=2)
eight=tk.Button(s_frame, text="8", width=5, height=2)
seven=tk.Button(s_frame, text="7", width=5, height=2)
div=tk.Button(s_frame, text="/", width=5, height=2)

#grid
nine.grid(row=2, column=2, padx=5,pady=5)
eight.grid(row=2, column=1, padx=5,pady=5)
seven.grid(row=2, column=0, padx=5,pady=5)
div.grid(row=2, column=3, padx=5,pady=5)

#2nd row
six= tk.Button(s_frame, text="6", width=5, height=2)
five= tk.Button(s_frame, text="5", width=5, height=2)
four= tk.Button(s_frame, text="4", width=5, height=2)
mult=tk.Button(s_frame, text="* ", width=5,height=2)

#grid
six.grid(row=2, column=2, padx=5,pady=5)
five.grid(row=2, column=1, padx=5,pady=5)
four.grid(row=2, column=0, padx=5,pady=5)
mult.grid(row=2, column=3, padx=5,pady=5)

#3rd row
three=  tk.Button(s_frame, text="3", width=5, height=2)
two=tk.Button(s_frame, text="2", width=5, height=2)
one=tk.Button(s_frame, text="1", width=5, height=2)
min=tk.Button(s_frame, text="- ",width=5, height=2)

#4th row
zero= tk.Button(s_frame, text="0", width=5, height=2)
clear= tk.Button(s_frame, text="C", width=5, height=2)
equal=tk.Button(s_frame, text="=", width=5, height=2)
add= tk.Button(s_frame, text="+ ", width=5, height=2)


frame.pack()
s_frame.pack()

window.mainloop()