import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return math.pi * self.__radius * self.__radius

    def get_circum(self):
        return math.pi * 2.0 * self.__radius

    # 객체의 현재 상태를 문자열로 요약
    def __str__(self):
        return "radius = " + str(self.__radius)

c = Circle(10)
print("원의 반지름 =", c.get_radius())
print("원의 넓이 =", c.get_area())
print("원의 둘레 =", c.get_circum())
print(c)
