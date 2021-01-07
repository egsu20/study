class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

    def __str__(self): # 생략하면 객체의 주소가 출력됨
        return 'Point('+str(self.x)+','+str(self.y)+')'

s1 = "Impossible "
s2 = "Dream"
s3 = s1.__add__(s2) # s1+s2와 같음
print(s3)

p1 = Point(2,3)
p2 = Point(3,2)
print(p1+p2)
