import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(4):
    t.forward(100)
    t.left(90)

t.up() # 펜을 듦
t.goto(-200, 0) # (-200, 0)으로 이동
t.down() # 펜을 내림

for i in range(4):
    t.forward(100)
    t.left(90)
