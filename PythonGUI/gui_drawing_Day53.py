# Create a program that allows users to draw on a canvas using a GUI

from tkinter import *
from tkinter import colorchooser


def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        current_color.set(color)

def start_drawing(event):
    global last_x, last_y, drawing
    last_x, last_y = event.x, event.y
    drawing = True

def draw(event):
    global last_x, last_y
    if drawing:
        x, y = event.x, event.y
        canvas.create_line(last_x, last_y, x, y, fill=current_color.get(), width=2)
        last_x, last_y = x, y

def stop_drawing(event):
    global drawing
    drawing = False

def clear_canvas():
    global canvas
    canvas.delete("all")


drawing_gui = Tk()
drawing_gui.title('Painting Canvas')
drawing_gui.geometry("%dx%d" % (drawing_gui.winfo_screenwidth(), drawing_gui.winfo_screenheight()))
drawing_gui.pack_propagate(False)
drawing_gui.resizable(0, 0)

current_color = StringVar()
current_color.set("black")
drawing = False

canvas = Canvas(drawing_gui, bg="white")
canvas.pack(fill=BOTH, expand=True)

choosecolor = Button(canvas, text="Choose Color",  width=20, command=lambda: choose_color(), font='Times 14')
choosecolor.place(x=600, y=10, height=30, anchor='c')
clearcanvas = Button(canvas, text="Clear",  width=20, command=lambda: clear_canvas(), font='Times 14')
clearcanvas.place(x=850, y=10, height=30, anchor='c')

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

drawing_gui.mainloop()
