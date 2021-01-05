from tkinter import *
from tkinter.colorchooser import *

window = Tk()
w = Canvas(window, width=300, height=200)
w.pack()
color = askcolor()

# color의 첫번째 요소는 rgb의 성분값.
# 두번째 요소는 rgb를 16진수로 표현한 문자열.
w.create_rectangle(50, 25, 200, 100, fill=color[1])
window.mainloop()
