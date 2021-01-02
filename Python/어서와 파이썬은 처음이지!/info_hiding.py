class Student:
    def __init__(self, name=None, age=0):
        # 정보 은닉 - private로 정의
        self.__name = name
        self.__age = age

    # setter
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        if age < 0 :
            self.__age = 0
        else:
            self.__age = age

    # getter
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

std = Student("Lee", 20)
print(std.get_name(), std.get_age())

std.set_age(21)
print(std.get_name(), std.get_age())


