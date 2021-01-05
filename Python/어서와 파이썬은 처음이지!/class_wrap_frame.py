from tkinter import *

class App:
    def __init__(self):
        window = Tk() # 지역 변수
        # fg : foreground
        helloB = Button(window, text="Hello",
                        command=self.hello, fg="red") 
        helloB.pack(side=LEFT)
        quitB = Button(window, text="Quit", command=self.quit)
        quitB.pack(side=LEFT)
        window.mainloop()

    def hello(self):
        print("Hello Button이 클릭됨")


    def quit(self):
        print("Quit Button이 클릭됨")

App() # App 클래스의 인스턴스 생성
