from tkinter import *

window = Tk()

Label(window, text="Times Font, red",
      fg="red", font="Times 32 bold italic").pack()

Label(window, text="Helvetica, blue",
      fg="blue", bg="yellow", font="Helvetica 32 bold italic").pack()

window.mainloop()
