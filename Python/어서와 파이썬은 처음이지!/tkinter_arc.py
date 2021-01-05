from tkinter import *

window = Tk()

canvas = Canvas(window, width = 300, height=200)
canvas.pack()

# 괄호 안 : 왼쪽 상단(x0, y0), 오른쪽 하단 (x1, y1)/ extent:각도 지정
canvas.create_arc(10, 10, 200, 150, extent=180, style=ARC)

window.mainloop()
