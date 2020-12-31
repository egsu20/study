a = [3,2,1,5,4]

# 비파괴적 sorted() 함수 - 내장 함수
print(a)
print(sorted(a))
print(a)
print("--------------------")

# 파괴적 sort() 함수 - 리스트 객체의 메소드
a.sort()
print(a)

# 조건을 가진 sorted - 공백으로 분리, 대소문자 가리지 않고 비교
print(sorted("A picture is worth a thousand words.".split(), key=str.lower))
