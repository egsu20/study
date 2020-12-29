# 상속 : 다른 클래스의 멤버 변수와 메소드 물려 받음
# 부모 클래스와 자식 클래스
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name,"이(가) 공격을 수행합니다. "\
            + "[전투력 : " + str(self.power) + "]")

# Monster가 Unit 클래스를 상속받음
class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    # 자식 클래스만의 멤버 함수 추가 가능
    def show_info(self):
        print("몬스터 이름 :", self.name)
        print("몬스터 종류 :", self.type)

unit = Unit("홍길동", 123)
unit.attack()
print()

monster = Monster("슬라임", 10, "초급")
monster.show_info()
monster.attack()