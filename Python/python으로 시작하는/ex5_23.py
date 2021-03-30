dict = {} # 빈 집합
dict = {3, 2, 3, 1}
print(dict)


fruits = ['사과', '오렌지', '포도', '오렌지']
fruits = set(fruits) # 중복 제거
print(fruits)

fruits.add('키위')
print(fruits)

fruits.update({'수박', '배'})
print(fruits)

fruits.remove('오렌지')
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)
