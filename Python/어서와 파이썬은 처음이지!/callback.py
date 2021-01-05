from tkinter import *

def callback():
    if button["text"] == "클릭":
        button["text"] = "click"
    else:
        button["text"] = "클릭"

window = Tk()
# command : 버튼과 함수의 연결
button = Button(window, text="클릭", command=callback)
button.pack()

window.mainloop()
