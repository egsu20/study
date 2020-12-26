list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)

print("# reversed() 함수")
print(list_reversed)
print(list(list_reversed))
print()

print("# reversed() 함수와 반복문")
for i in list(list_reversed):
    print("-", i)
