from tkinter import *

window = Tk()

w = Canvas(window, width=300, height=200)
w.pack()

i = w.create_line(0, 0, 300, 200, fill="red")
# 좌표 변경
w.coords(i, 0, 0, 300, 100)
# 색상 변경
w.itemconfig(i, fill="blue")

# 항목 삭제
# w.delete(i)
# w.delete(All)
window.mainloop()
