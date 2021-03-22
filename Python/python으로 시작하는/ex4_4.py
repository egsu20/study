import turtle
import math

turtle.shape("turtle")
turtle.forward(100)

turtle.right(90)
turtle.forward(100)

turtle.right(90+45)
turtle.forward(math.sqrt(100*100*2))

turtle.left(45)
turtle.forward(100)

turtle.left(90)
turtle.forward(100)

turtle.left(45+90) # 이 부분 생략 시 거북이는 아래를 가리킴
turtle.goto(0,0)
