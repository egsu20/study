import random

# 정수 범위의 난수
print(random.randint(1, 6))

# random()은 0~1 사이의 난수 반환
print(random.random() * 100)

# 주어진 시퀀스의 항목을 임의로 반환
mylist=["one", "two", "three"]
print(random.choice(mylist))

# 리스트 항목을 임의로 섞음
mylist = [[x] for x in range(10)]
random.shuffle(mylist)
print(mylist)
