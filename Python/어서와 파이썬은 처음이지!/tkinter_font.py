import tkinter as tk
import tkinter.font as font

class App:
    def __init__(self):
        root=tk.Tk()

        # 폰트 객체 생성
        self.customFont = font.Font(family="Helvetica", size=12)

        buttonframe = tk.Frame()
        label = tk.Label(root, text="Hello", font=self.customFont)
        buttonframe.pack()
        label.pack()

        # 클릭 시 BigFont 호출
        bigger = tk.Button(root, text="폰트 크게", command=self.BigFont)
        # 클릭 시 SmallFont 호
        smaller = tk.Button(root, text="폰트 작게", command=self.SmallFont)
        bigger.pack()
        smaller.pack()

        root.mainloop()

    def BigFont(self):
        size = self.customFont["size"]
        # 폰트 객체의 configure로 폰트 속성 변
        self.customFont.configure(size=size+2)

    def SmallFont(self):
        size = self.customFont["size"]
        self.customFont.configure(size=size-2)


App()
