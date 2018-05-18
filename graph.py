from tkinter import *

window = Tk()
width1 = 100
height1 = 100
canvas = Canvas(window, width=300, height=300, background='blue')
canvas1 = Canvas(window, width=300, height=300, background='green')


canvas.create_oval(10,10,width1,height1,fill='white',tags='circle1')
def keycheck(event):
    global width1
    global height1
    print("keycode? ", event.keycode)
    if event.keycode == 37:
        width1 = width1 + 10
        canvas.delete('circle1')
        canvas.create_oval(10, 10, width1, height1, fill='white', tags='circle1')
        canvas.update()
    elif event.keycode == 38:
        height1 = height1 + 10
        canvas.delete('circle1')
        canvas.create_oval(10, 10, width1, height1, fill='white', tags='circle1')
        canvas.update()
canvas.bind("<Key>", keycheck)
canvas.pack()
canvas1.pack()
canvas.focus_set()

window.mainloop()