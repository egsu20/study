nums = [1,1,1,2,2,3,3,2,3,3,1]
def max_count(nums):
    counts = {}
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

counts = max_count(nums)
first = []
max_num = max(counts.values())
for name, count in counts.items():
    print(name, ':', count, '번')
    if count == max_num:
        first.append(name)

print('1등 :', first)
