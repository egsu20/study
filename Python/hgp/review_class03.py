class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕 " + to_name + "야~")

    def introduce(self):
        print("나는 " + self.name + "(이)라고 해. "\
            + "나는 " + str(self.age) + "살이야")

# Person을 상속받는 Police
class Police(Person):
    def arrest(self, to_arrest):
        print(to_arrest + ", 넌 체포되었다.")

# Person을 상속받는 Programmer
class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다 : " + to_program)

print("# Person 클래스 사용")
jenny = Person("jenny", 21)
wonie = Person("wonie", 21)

jenny.say_hello("철수")
jenny.introduce()

wonie.say_hello("영희")
wonie.introduce()
print()

print("# Police 클래스 사용")
pol = Police("pol", 21)
pol.introduce() # Police가 Person을 상속받기 때문에 가능
pol.arrest("thief")
print()

print("# Programmer 클래스 사용")
pro = Programmer("pro", 21)
pro.introduce()
pro.program("chatting program")
print()