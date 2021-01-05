# 엔트리 위젯 - 사용자의 입력을 한 줄 받음
from tkinter import *

def show():
    # get : 엔트리 내용 가져옴
    print("이름: {}\n나이: {}".format(e1.get(), e2.get()))

window = Tk()

# 배치 관리자는 grid
Label(window, text="이름").grid(row=0)
Label(window, text="나이").grid(row=1)

e1 = Entry(window)
e2 = Entry(window)

# grid에 배치
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window, text="보이기", command=show).grid(row=3,
        column=1, sticky=W, pady=4) # sticky : 위치조정
Button(window, text="종료", command=window.quit).grid(row=3,
        column=0, sticky=W, pady=4)

mainloop()
