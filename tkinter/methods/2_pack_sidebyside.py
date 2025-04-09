import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.geometry("400x400")
window.title("Pack Method Tutorial")

pane = tk.Frame(window)
pane.pack(fill = BOTH, expand= True)

#button widgets with side to make it side by side
b1= tk. Button(pane,text= "Click Me !", background="sky blue", fg= "white")
b1.pack(side = LEFT, expand =True,fill= X)

b2= tk. Button(pane,text= "Click Me 2!", background="red", fg= "white")
b2.pack(side = LEFT, expand =True,fill= X)

b3= tk. Button(pane,text= "button me also!", background="light pink", fg= "white")
b3.pack(side = LEFT, expand =True,fill= X)

window.mainloop()

