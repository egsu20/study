# 다중 텍스트 입력
from tkinter import *

window = Tk()

t = Text(window, height=5, width=60)
t.pack()
# END : 텍스트를 끝에 추가
t.insert(END, "텍스트 위젯은 여러줄의 \n텍스트 표시 가능")

window.mainloop()
