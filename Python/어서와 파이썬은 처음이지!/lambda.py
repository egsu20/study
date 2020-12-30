sum = lambda x,y : x+y

print("sum =",sum(10,20))
print("sum =",sum(20,10))
print()

L = [lambda x : x**2,
        lambda x : x**3,
        lambda x : x**4]

for f in L:
    print(f(3))
print()

min = (lambda x,y: x if x<y else y)
print(min(1000,200))