class Animal:
    def __init__(self, name=""):
        self.name = name
    def eat(self):
        print("먹이를 먹고 있습니다.")

class Dog(Animal):
    def __init__(self):
        # 부모 클래스의 생성자를 명시적으로 호출
        super().__init__()

    # 오버라이딩
    def eat(self):
        print("강아지가 먹고있습니다.")

dog = Dog()
dog.eat()
