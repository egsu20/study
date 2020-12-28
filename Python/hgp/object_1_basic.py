students = [
    {"name":"A","korean":87, "math":98},
    {"name":"B","korean":96, "math":47},
    {"name":"C","korean":78, "math":88},
    {"name":"D","korean":84, "math":96},
    {"name":"E","korean":91, "math":67}
]

# 학생 한 명씩 출력
print("이름", "총점", "평균", sep="\t")
for student in students:
    # 점수의 총합과 평균
    score_sum = student["korean"]+ student["math"]
    score_average = score_sum / 2

    # output
    print(student["name"], score_sum, score_average, sep="\t")