# q 5.16.1
def times1(a):
    for i in range(len(nums)):
        a[i] = a[i]*2
    print(a)
         
nums = [1,2,3]
times1(nums)
print()

# q 5.16.2
def times2(k):
    k[0] = k[0]*2
    k[1] = k[1]*2

a = [1,2]
b = [3,4]

times2(a)
times2(b)
print('a=',a,'b=',b)
print()

# q 5.16.3
fruitdb = [['사과', 1020],['오렌지',880],['포도', 3160]]
for i in range(len(fruitdb)):
    print(fruitdb[i][0], end = ' ')
print('\n')
# q 5.16.4
for i in range(len(fruitdb)):
    print('* 과일명 :', fruitdb[i][0], '(', fruitdb[i][1],')원')
print()

# q 5.16.5
sum = 0
for i in range(len(fruitdb)):
    sum += fruitdb[i][1]
avg = sum/len(fruitdb)
print('%.1f원' % avg)
