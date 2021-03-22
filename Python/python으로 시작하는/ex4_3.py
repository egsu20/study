def swap(a, b):
    return b, a

a = 3
b = 5
print("swap() 호출 전 :", a, b)
a, b = swap(a,b)

print("swqp() 호출 후 :", a, b)
