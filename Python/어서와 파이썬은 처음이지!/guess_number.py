print("숫자게임에 오신 것을 환영합니다.")

number = 7

while True:
    guess = int(input("1부터 10 사이의 숫자를 추측해보세요(종료는 -1) : "))

    if guess == -1:
        print("프로그램 종료")  
        break
    if guess < 1 or guess > 10 :
        print("1부터 10 사이의 숫자만 입력하세요!")
        continue

    if guess == number :
        print("맞았습니다")
        break
    elif guess > number:
        print("더 작은 수를 입력하세요")
    else:
        print("더 큰 수를 입력하세요")
 
