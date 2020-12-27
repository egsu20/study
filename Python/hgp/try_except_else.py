# try except else
try:
    user_input = int(input("정수 입력 : "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("radius :", user_input)
    print("circumference :", user_input * 3.14 * 2)
    print("area :", 3.14 * user_input * user_input)