#단수 반환
def add(a, b):
    return a+b

#복수 반환
def sum_add(a, b):
    sum = a+b
    diff = a-b
    return sum, diff

print(add(3,5))
print(sum_add(5,3))

