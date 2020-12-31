STUDENTS = 5

scores = []
score_sum = 0.0
count = 0

for i in range(STUDENTS):
    n = int(input("성적을 입력하시오 : "))
    
    scores.append(n)
    score_sum += n

    if n >= 80:
        count += 1

print("성적 평균은", score_sum / STUDENTS,"입니다.")
print("80점 이상 성적을 받은 학생은",count,"명입니다.")
