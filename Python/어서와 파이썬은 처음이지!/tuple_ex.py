# 리스트로부터 튜플 생성
t = tuple([1,2,3,4,5])
print("t :", t)

# 튜플 내부에 다른 튜플 포함
u = t, (6,7,8,9,10)
print("u :", u)

# 튜플 반복
print(("Hi",)*4)

# 괄호없이 나열된 객체도 튜플로 인식

# 튜플 대입 연산
student = ("철수", 21, "CS")
(name, age, major) = student
print(name)
print(age)
print(major)
