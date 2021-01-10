class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '알 수 없음'

class Dog(Animal):
    def speak(self):
        return "멍멍"

class Cat(Animal):
    def speak(self):
        return "야옹"


animal = [Dog('d1'),
          Dog('d2'),
          Cat('c1')]

for a in animal:
    print(a.name + " : " + a.speak())
