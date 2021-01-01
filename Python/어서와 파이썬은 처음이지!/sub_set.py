# 부분 집합 검사
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
print(b.issubset(a))

# 상위 집합 검사
a = {1,2,3,4,5}
b = {1,2,3}
print(a.issuperset(b))

a = {1,2,3}
b = {3,4,5}

# 합집합
print(a | b)
print(a.union(b))
print(b.union(a))

# 교집합
print(a & b)
print(a.intersection(b))

# 차집합
print(a-b)
print(a.difference(b))
