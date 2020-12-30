import turtle
t = turtle.Pen()

t.shape("turtle")

while True:
    input_a = input("왼쪽=left, 오른쪽=right: ")

    if input_a == "left":
        t.left(60)
        t.forward(50)
    else:
        t.right(60)
        t.forward(50)
