from tkinter import *

window = Tk()

# 이미지 객체 생성
photo = PhotoImage(file="a1.gif")
# 이미지 출력. photo를 image 매개변수로 전달
w = Label(windowm image=photo)
w.photo = photo
w.pack()

window.mainloop()
