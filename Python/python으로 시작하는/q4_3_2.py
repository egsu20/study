import turtle
import random

col = random.randint(0,2)
if col == 0:
    turtle.pencolor('plum')
elif col == 1:
    turtle.pencolor('yellow')
elif col == 2:
        turtle.pencolor('blue')
        
turtle.circle(50)
