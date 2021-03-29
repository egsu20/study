nums = [0,1,2,3,4,5]
del nums[1]
print(nums)

nums = [0,1,2,3,4,5]
del nums[1:5]
print(nums)
print()

nums = [0,1,2,3,4,5]
nums.pop()
nums.pop()
print(nums)

nums = [0,1,2,3,4,5]
nums.pop(2)
print(nums)
print()

nums = [0,1,2,3,4,5]
nums[1:2] = []
print(nums)
