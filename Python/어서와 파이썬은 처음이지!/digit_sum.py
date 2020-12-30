num = 1234
sum = 0

while num > 0:
    sum += num % 10
    num = num // 10

print("자리수의 합은 %d입니다" % sum)
    
    
