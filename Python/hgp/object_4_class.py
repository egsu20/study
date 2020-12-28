class Student:
    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math
        print("{} - 생성되었습니다".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

students = [ 
    Student("A", 87, 98),
    Student("B", 97, 86),
    Student("C", 99, 43),
    Student("D", 76, 96),
    Student("E", 98, 78)
]

for i in range(len(students)):
    print(students[i].name, students[i].korean, students[i].korean, sep="\t")
