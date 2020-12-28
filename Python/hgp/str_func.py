class Student:
    def __init__(self,name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math

    def get_sum(self):
        return self.korean + self.math

    def get_average(self):
        return self.get_sum() / 2

    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

students = [
    Student("A", 87, 98),
    Student("B", 97, 86),
    Student("C", 99, 43),
    Student("D", 76, 96),
    Student("E", 98, 78)
]

print("name","sum","avg",sep="\t")
for student in students:
    print(str(student))