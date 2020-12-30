# square
def square(n):
    return n * n


# max
def max_value(x,y):
    if x > y:
        return x
    else:
        return y

# 전방 선언한 함수가 power 함수 호출 가능
def main():
    print(power(2,4))

# power
def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

print(square(10))
print(max_value(10,20))
print(power(10,2)) # 10**2
main()