def create_student(name, korean, math):
    return {
        "name": name,
        "korean" : korean,
        "math" : math
    }

students = [
    create_student("A", 87, 98),
    create_student("B", 97, 86),
    create_student("C", 99, 43),
    create_student("D", 76, 96),
    create_student("E", 98, 78)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"]
    score_average = score_sum / 2

    print(student["name"], score_sum, score_average, sep="\t")