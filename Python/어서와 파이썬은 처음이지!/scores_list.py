# 빈 리스트 생성
scores = []

for i in range(10):
    scores.append(int(input("성적 입력 : ")))

print(scores)

for value in scores:
    print(value, end=" ")
