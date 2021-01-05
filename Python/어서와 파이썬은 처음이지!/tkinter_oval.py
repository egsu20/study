from tkinter import *

window = Tk()

canvas = Canvas(window, width=300, height=200)
canvas.pack()

# 괄호 안 : x0, y0, x1, y1, ...
canvas.create_oval(10, 10,200, 150, fill="black")

window.mainloop()
