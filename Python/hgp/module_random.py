import random # random의 반복 사용을 줄이기 위해 from random import random, randrange, uniform, choice ....
print("# random 모듈")

# random() : 0.0 <= x < 1.0 사이의 float 리턴
print("random() :", random.random())

# uniform(min, max) : 지정한 범위 사이의 float 리턴
print("uniform() :", random.uniform(10,20))

# randrange() : 지정한 범위의 int 리턴
# randrange(max) : 0 ~ max
# randrange(min, max) : min ~ max 사이의 값
print("randrange(10) :", random.randrange(10))

# choice(list) : 리스트 내부 요소 중 랜덤 선택
print("choice([1,2,3,4,5]) :", random.choice([1,2,3,4,5]))

# chuffle(list) : 리스트 요소들을 랜덤하게 섞음
print("shuffle([1,2,3,4,5]) :", random.shuffle([1,2,3,4,5]))

# sample(list, k=number) : 리스트 요소 중 k개 선택
print("sample([1,2,3,4,5], k=2) :", random.sample([1,2,3,4,5], k=2))