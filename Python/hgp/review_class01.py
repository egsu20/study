# 클래스 : 객체지향 프로그래밍이 가능하게 해주는 기본적인 단위,
#          소스코드의 중복 최소화
# 인스턴스 : 클래스로 찍어낸 객체
# 클래스 멤버 : 클래스 내부 변수
# 클래스 함수 : 클래스 내부 함수

class Car:
    # 생성자, 첫 번째 매개변수로 self
    def __init__(self, name, color): 
        self.name = name # 클래스 멤버 (객체의 속성)
        self.color = color
    # 클래스 메소드
    def show_info(self):
        print("name :",self.name)
        print("color :",self.color)
    # Setter 메소드
    def set_name(self, name):
        self.name = name
    def set_color(self, color):
        self.color = color
    # 소멸자
    def __del__(self):
        print(self.name, "이 소멸됨")
        
car1 = Car("sonata","red")
car1.show_info()

car2 = Car("avante","black")
car2.show_info()
print()

del car2 # 소멸자 실행
print()

print(car1.name,"을(를) 구매했습니다")
print()

car1.set_name("volkswagen")
print(car1.name,"로 변경되었습니다")