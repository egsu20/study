fact = 1.0
num = int(input("정수 입력 : "))

for i in range(1, num+1):
    fact *= i

print(str(num)+"! =", fact)
    
