# tkinter 모듈 포함
from tkinter import *

# 루트 윈도우 생성.
window = Tk()

# window의 자식으로 Label 위젯 생성
label = Label(window, text="Hello World!")
# 위젯 크기 조정. 위젯 출력 시 필요
# 배치 관리 이벤트 추가
label.pack()

# 사용자의 입력이나 윈도우 시스템 이벤트 등을 처리할 이벤트 루프
# 윈도우가 이벤트 루프에 들어가야만 화면에 출력
window.mainloop()
