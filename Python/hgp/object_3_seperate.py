# 학생에 대한 딕셔너리 리턴
def create_student(name, korean, math):
    return {
        "name": name,
        "korean" : korean,
        "math" : math
    }

# 학생 처리
def student_get_sum(student):
    return student["korean"] + student["math"]

def student_get_average(student):
    return student_get_sum(student) / 2

def student_to_string(student):
    return "{}\t{}\t{}\t".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student))

students = [
    create_student("A", 87, 98),
    create_student("B", 97, 86),
    create_student("C", 99, 43),
    create_student("D", 76, 96),
    create_student("E", 98, 78)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))