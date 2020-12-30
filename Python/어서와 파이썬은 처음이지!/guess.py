import random

tries = 0
number = random.randint(1,10)

print("1부터 10 사이의 숫자를 맞추시오")

while tries < 10:
    n = int(input("숫자를 입력하시오 : "))
    tries += 1
    
    if n == number:
        print("축하합니다. 시도횟수 =",tries)
        break

    if tries == 10:
        print("실패!")
        break
    
    if n > number:
        print("높음!")
    elif n < number:
        print("낮음!")
