from copy import deepcopy

scores = [10,20,30,40,50]
print(scores)

# 깊은 복사 - 1
values = list(scores)

values[2] = 99
print(scores)
print(values)

# 깊은 복사 - 2
values = deepcopy(scores)

# 얕은 복사
values = scores
values[2] = 33
print(scores)
