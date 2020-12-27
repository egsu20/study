PI = 3.141592

def number_input():
    output = input("숫자 입력 : ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# 현재 파일이 진입점(entry point 또는 main)일 때만 실행
# 다른 파일에서 import 되어 실행되는 경우엔 실행되지 않음
if __name__ == "__main__": 
    print("get_circumference(10) :", get_circumference(10))
    print("get_circle_area(10):", get_circle_area(10))