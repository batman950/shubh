from tkinter import *

window = Tk()
canvas = Canvas(window,width=400,height=400,bg="#00ff00")

canvas.create_line(10,300,300,300,width="5",fill="white")

canvas.create_oval(200,200,300,300,width="5",fill="blue")
canvas.create_rectangle(100,100,200,200,width="5",fill="green")

canvas.create_text(100,100,text="hello",fill="red")

canvas.create_polygon(10,10,200,40,150,350,fill="green")
canvas.create_arc(10,10,200,200,style="pieslice",extent="45",fill="white")


canvas.pack()
Tk.mainloop(canvas)

