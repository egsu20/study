# dir() : 객체가 가진 변수와 함수 리턴
print(dir([1,2,3]))
print()

# divmod(x, y) : x/y 몫과 나머지를 튜플 형태로 반환
# 이때 x, y가 정수이면 정수 나누기가 됨
print(divmod(10,3))

# enuberate(iterable, start=0) :
# 요소의 번호와 그 번호에 해당하는 값을 갖는 객체
for i, str in enumerate(["aaa", "bbb", "ccc"]):
    print(i, str)

# eval() : 수식을 문자열로 받아서 실행
exp = input("파이썬의 수식을 입력하시오 : ")
print(eval(exp))

# range(start, stop, step) : start와 step은 선택사항
# stop-1까지의 항목을 포함
print(list(range(5)))

# sorted(iterable, key, reverse) :
# iterable 객체의 항목들을 정렬한 리스트를 반환
print(sorted([5,2,3,1,4]))

# sum() : 리스트에 존재하는 항목을 전부 더함
print(sum([1,2,3,4,5]))
