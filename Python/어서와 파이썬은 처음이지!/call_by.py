# call_by_value
def func1(x):
    print("----- func1 -----")
    print(x, id(x))
    x = 28
    print(x, id(x))
    print("----- ----- -----")

# call_by_reference
def func2(list):
    list[0] = 99

#func1 호출
y = 10
print(y, id(y))
func1(y)
print(y, id(y))
print()

#func2 호출
values = [0, 1, 1, 2, 3, 5, 8]
print(values)
func2(values)
print(values)
