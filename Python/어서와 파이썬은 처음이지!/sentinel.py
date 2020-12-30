n = 0
sum = 0
score = 0

print("종료하려면 음수를 입력하시오")
while True:
    score = int(input("성적을 입력하시오 : "))
    if score < 0:
        break;
    sum += score
    n += 1

print("성적의 평균은 %f입니다" % (sum/n))
