class Student:
    count = 0

    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math

        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

students = [
    Student("A", 87, 98),
    Student("B", 97, 86),
    Student("C", 99, 43),
    Student("D", 76, 96),
    Student("E", 98, 78)
]

print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))