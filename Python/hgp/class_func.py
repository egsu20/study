class Student:
    #클래스 변수
    count = 0
    students = []

    #클래스 함수
    @classmethod
    def print(cls):
        print("----- student list -----")
        print("name\tsum\tavg")
        for student in cls.students:
            print(str(student))
        print("----- ------------ -----")

    def __init__(self,name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math

    def get_average(self):
        return self.get_sum() / 2

    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())


Student("A", 87, 98)
Student("B", 97, 86)
Student("C", 99, 43)
Student("D", 76, 96)
Student("E", 98, 78)

# 현재 생성된 학생 전부 출력
Student.print()