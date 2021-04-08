people = ['홍', '홍','김','이','홍','김']
nums = [1,1,1,2,2,3,2,3,3,3,3,1]

import scipy.stats as ss

mode, count = ss.mstats.mode(people)
print(mode, count)

mode2, count2 = ss.mstats.mode(nums)
print(mode, count)
