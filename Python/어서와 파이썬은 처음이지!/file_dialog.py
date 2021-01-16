from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

read_file = askopenfilename()
if read_file != None:
    infile = open(read_file,"r")
for line in infile.readlines():
    line = line.strip()
    print(line)

infile.close()
