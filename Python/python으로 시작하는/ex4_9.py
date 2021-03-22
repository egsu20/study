import turtle
import random
for i in range(10):
    for j in range(5):
        col = random.randint(0, 4)
        if(0 == col):
            turtle.color("red")
        elif(1 == col):
            turtle.color("blue")
        elif(2 == col):
            turtle.color("green")
        elif(3 == col):
            turtle.color("purple")
        elif(4 == col):
            turtle.color("yellow")
        sel = random.randint(0,4)
        if(0 == sel):
            turtle.forward(random.randint(50,100))
        elif(1 == sel):
            turtle.right(random.randint(90,360))
        elif(2 == sel):
            turtle.begin_fill()
            turtle.circle(random.randint(-100,-20))
            turtle.end_fill()
        elif(3 == sel):
            turtle.forward(random.randint(30, 50))
        elif(4 == sel):
            turtle.circle(random.randint(20, 100))

    a = float(random.randint(-300, 300))
    b = float(random.randint(-300,300))
    turtle.goto(a,b)
        
