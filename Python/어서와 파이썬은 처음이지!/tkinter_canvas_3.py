from tkinter import *

window = Tk()
w = Canvas(window, width=300, height=200)
w.pack()

# fill은 도형의 색상을 채움. coutline은 경계선의 색상칠함.
# fill은 rgb를 16진수로 표현한 것
w.create_rectangle(50, 25, 200, 100, outline="blue", fill="#FA88AB")

window.mainloop()
