number = int(input("정수 입력 : "))

if number % 2 == 0:
    print((
        "입력한 문자열은 {}\n"
        "{}는 짝수"
    ).format(number,number))
else:
    print((
        "입력한 문자열은 {}\n"
        "{}는 홀수"
    ).format(number,number))