# 존재 여부
dice = (3,2,5,3,4)
print(2 in dice)
print(2 not in dice)
print()

# 반복
a = (1,2,3)
b = a*2
print(b)
print()

# 원소의 개수 측정
print(len(dice))
print()

# 찾기
print(dice.count(3))
print(dice.index(2))
print()
# reverse(), sort() 안됨

# 2차원 튜플
dice1 = (6,1,4)
dice2 = (5,2,1)
result = (dice1, dice2)
print(result)
print(result[1][1])
