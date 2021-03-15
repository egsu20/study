# 온도에 따른 물 상태 출력
temp = float(input("온도 입력 : "))

print("물의 상태는 ", end="")

if temp <= 0:
    print("얼음")
elif temp > 0 and temp < 100:
    print("액체")
else:
    print("기체")
