# try - except
try:
    user_input = int(input("정수 입력 : "))

    print("radius :", user_input)
    print("circumference :", user_input * 3.14 * 2)
    print("area :", 3.14 * user_input * user_input)
except:
    print("error")
