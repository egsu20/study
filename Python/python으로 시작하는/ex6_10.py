#students = [
#    {"name":"윤인성", "korean":87, "math": 98, "english":88, "science":95},
#    {"name":"윤인성2", "korean":87, "math": 98, "english":88, "science":95}
#    {"name":"윤인성3", "korean":87, "math": 98, "english":88, "science":95}
#]
#print("이름", "총점", "평균", sep="\t")

def create_student(name, korean, math, english, science):
    return {
            "name" :name,
            "korean": korean,
            "math":math,
            "english":english,
            "science"science
        }

    def student_get_sum(student):
        return student["korean"] + student["math"] +\
               student["english"] + student["science"]

    def student_get_averate(student):
        return student_get_sum(student) / 4

    def student_to_string(student):
        return "{}\t{}\t{}".format(
            student["name"],
            student_get_sum(student),
            student_get_average(student))
