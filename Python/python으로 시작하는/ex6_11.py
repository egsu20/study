class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english= english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
               self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 87, 98, 88, 95),
    Student("구지연", 87, 98, 88, 95),
    Student("나선주", 87, 98, 88, 95),
]

for i in range(4):
    print(students[i].name)
