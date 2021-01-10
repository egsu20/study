class Person():
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return "이름 : " + self.name +"\n"+\
               "주민번호 : " + str(self.number)+"\n"


class Student(Person):
    def __init__(self, name, number, classes, gpa=0):
        super().__init__(name, number)
        self.classes = classes
        self.gpa = gpa

    def __str__(self):
        string = super().__str__()
        return string + "수강과목 : " + self.classes + "\n" +\
               "평점 : " + str(self.gpa) + "\n"
        

class Teacher(Person):
    def __init__(self, name, number, courses, salary):
        super().__init__(name,number)
        self.courses = courses
        self.salary = salary

    def __str__(self):
        string = super().__str__()
        return string + "강의과목 : " + self.courses + "\n" +\
               "월급 : " + str(self.salary) + "\n"

std = Student("hong", 12345678, "자료구조")
teac = Teacher("kim", 123456790, "Python", 300000)

print(std)
print(teac)
