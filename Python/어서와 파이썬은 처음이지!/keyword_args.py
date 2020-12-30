# 디폴트 인수
def add(a = 1, b = 1):
    return a + b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b=1):
    return a / b

print(add())
print(subtract(b = 2,a = 5))
print(multiply(a = 2, b = 5 ))
print(divide(4, 2))