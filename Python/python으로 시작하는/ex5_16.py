# 2차원 리스트
fruitdb = [['사과', 1020],['오렌지', 880],['포도', 3160]]
print(fruitdb[1])
print(fruitdb[1][0])

record = [
    [1,2,3],
    [10,20,30],
    [100,200,300]]

index = [ary[1] for ary in record]
print(index)

mylist = [[1,2], [3,4,5], [6,7]]
newlist = [x for x in mylist if len(x)==2]
print(newlist)
