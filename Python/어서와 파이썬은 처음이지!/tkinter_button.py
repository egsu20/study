from tkinter import *

window = Tk()

b1 = Button(window, text="first button")
b2 = Button(window, text="second button")
# 압축 배치 관리자. 디폴트값은 Top
# padx : 좌우 패딩 추가, pady : 상하 패딩 추가
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)

# 버튼의 텍스트 변경
b1["text"] = "one"
b2["text"] = "Two"

window.mainloop()
