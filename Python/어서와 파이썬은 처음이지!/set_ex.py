# 여러 가지 자료형이 섞인 자료형
myset = {1.0, 2.0, "Hello world", (1,2,3)}
print(myset)

# 빈 세트 생성
numbers = set()
print(numbers)

# 세트는 모든 요소를 해승으로 이용하여 저장, 관리
# 따라서 세트의 모든 값은 해싱 가능하여야 하며,
# 변경 되는 항복이어선 안된다.
# ex : numbers = {1,2,[3,4,5]}

# 문자열, 리스트로부터의 세트 생성은 가능
print(set([1,2,3,1,2,3]))
print(set("abcdefa")) # 중복을 허용하지 않음

numbers = {2,1,3}

# 요소 추가
numbers.add(4)
print(numbers)

# 여러개의 요소 추가
# 마찬가지로 중복 요소는 포함 x
numbers.update([2,3,4,5])
print(numbers)

# 요소 삭제 - 1
numbers.discard(5)
print(numbers)
# 요소 삭제 - 2
numbers.remove(4)
print(numbers)

# 전체 삭제
numbers.clear()
print(numbers)


