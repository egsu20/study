# 전역변수 PI 사용
PI = 3.141592

def circleArea(radius):
    return PI * radius * radius

def circleCircumference(radius):
    return 2 * PI * radius

radius = float(input("원의 반지름 입력 : "))
print("원의 면적:", circleArea(radius))
print("원의 둘레:", circleCircumference(radius))