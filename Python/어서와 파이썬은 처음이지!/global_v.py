def sub():
    global s # 외부의 전역 변수 사용
    print(s)
    s = "떡볶이 먹고싶" # 전역 변수가 변경됨
    print(s)

s = "떡볶이가 좋음!"
sub()
print(s)