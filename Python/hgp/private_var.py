import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi* self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10)
print("circumference :",circle.get_circumference())
print("area :", circle.get_area())
print()


# corcle.__radius와 같이 
# 클래스 외부에서 클래스의 프라이빗 변수 __radius에 접근하면 ERROR!