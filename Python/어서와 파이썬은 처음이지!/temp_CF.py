def C2F(temp):
    return 9.0 / 5.0 * temp +32.0

def F2C(temp):
    return (temp - 32.0) * 5.0 / 9.0

while True:
    print("  'c' 섭씨온도에서 화씨온도로 변환")
    print("  'f' 화씨온도에서 섭씨온도로 변환")
    print("  'q' 종료")

    char = input("메뉴에서 선택 : ")
    if char == 'q':
        print("프로그램 종료")
        break

    elif char == 'c':
        temp = float(input("섭씨온도: "))
        print(C2F(temp))

    elif char == 'f':
        temp = float(input("화씨온도: "))
        print(F2C(temp))

    else:
        print("올바른 메뉴 선택 바람")