import turtle
import random
for i in range(3):
    col = random.randint(0, 2)
    sel = random.randint(0, 1)
    if(col == 0):
        turtle.pencolor('yellow')
    elif (col == 1):
        turtle.pencolor('blue')
    elif(col == 2):
        turtle.pencolor('red')
    if(sel == 0):
        turtle.forward(100)
    elif (sel == 1):
        turtle.circle(50)
    turtle.right(45)
