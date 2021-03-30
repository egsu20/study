import turtle
import random

for i in range(10):
    for j in range(5):
        # 튜플을 이용하여 turtle의 펜 색상과 색상 변경
        coltype = ('yellow', 'blue', 'red', 'purple', 'green')
        col = random.randint(0,4)
        turtle.pencolor(coltype[col])
        col = random.randint(0,4)
        turtle.color(coltype[col])
        
        sel = random.randint(0,4)
        if(0==sel):
            turtle.forward(random.randint(30,50))
        elif(1==sel):
            turtle.right(random.randint(90,360))
        elif(2==sel):
            turtle.begin_fill()
            turtle.circle(random.randint(-100,-20))
            turtle.end_fill()
        elif(3==sel):
            turtle.forward(random.randint(30,50))
        elif(4==sel):
            turtle.circle(random.randint(20,100))

    a = float(random.randint(-300, 300))
    b = float(random.randint(-300, 300))
    turtle.goto(a,b)
