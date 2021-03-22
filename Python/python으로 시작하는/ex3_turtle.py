import turtle

t = turtle.Turtle()

t.shape("turtle")
t.width(3)
t.shapesize(3,3)

while True:
    com = input("명령을 입력하시오 : ")
    if com == "l":
        t.left(90)
        t.forward(100)
    elif com == "r":
        t.right(90)
        t.forward(100)
    elif com == "q":
        break

turtle.bye()
