user_input = input("정수 입력 : ")

# digit
if user_input.isdigit():
    user_input = int(user_input)

    print("radius :", user_input)
    print("circumference :", user_input * 3.14 * 2)
    print("area :", 3.14 * user_input * user_input)

else:
    print("not digit")