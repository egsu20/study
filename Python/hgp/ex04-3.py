max_value = 0
a = 0
b = 0

for i in range(1,100+1):
    j = 100 - i

    mul = 0
    mul = i * j

    if max_value < mul:
        max_value = mul
        a = i
        b = j
        
print("최대가 되는 경우 : {} * {} = {}".format(a,b,max_value))