import random

x = random.randint(1, 10)
y = random.randint(1, 10)

answer = int(input("{x} + {y} = "))

flag = (answer == (x+y))
print(flag)
print(x, ",", y)
