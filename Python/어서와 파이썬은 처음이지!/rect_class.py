class Rectangle:
    def __init__(self, side = 0):
        self.side = side

    def get_area(self):
        return self.side * self.side

# 객체를 함수로 전달
def print_area(r, n):
    # 객체의 변의 길이를 1씩 증가시키며
    # 넓이 출력을 n번 반복
    while n >= 1:
        print(r.side, "\t", r.get_area())
        r.side = r.side+1
        n = n-1

rect = Rectangle()
count = 5
print_area(rect, count)
print("사각현의 변 :", rect.side)
print("반복 횟수 :", count)
