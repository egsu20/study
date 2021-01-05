from tkinter import *

def color_change():
    btn["fg"]="#ff0000"
    btn["bg"]="#00ff00"

window = Tk()

btn = Button(window, text="버튼을 클릭하세요.", command=color_change)
btn.pack()
btn["fg"]="yellow" # 전경색
btn["bg"]="green" # 배경색

