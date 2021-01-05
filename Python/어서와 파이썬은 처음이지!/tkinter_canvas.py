from tkinter import *

window = Tk()
# Canvas의 생성자를 호출하여서 300X200 크기의 캔버스 생성
w = Canvas(window, width=300, height=200)
w.pack()

# 순서대로 x, y, 사각형의 width, height
w.create_line(0, 0, 300, 200)
w.create_line(0, 0, 300, 100, fill="red")
w.create_rectangle(50, 25, 200, 100, fill="blue")

window.mainloop()
