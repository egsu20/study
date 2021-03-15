import turtle

t = turtle.Turtle()
# 거북이 모양
t.shape("turtle")
# 선 굵기
t.width(3)
# 3배 확대
t.shapesize(3,3)

while True:
    command = input("명령을 입력하시오(l, r, q) : ")
    if command == "l":
        t.left(90) # 방향
        t.forward(100) # 앞으로
    elif command == "r":
        t.right(90)
        t.forward(100)
    elif command == "q":
        break
    else:
        continue

turtle.mainloop()
turtle.bye()
