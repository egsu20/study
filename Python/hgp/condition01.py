num = input("정수 입력 : ")

num_char = num[-1]
number = int(num_char)

if number == 0\
    or number == 2\
    or number == 4\
        or number == 6\
            or number == 8:
            print("짝수")

if number == 1\
    or number == 3\
      or number == 5\
          or number == 7\
              or number == 9:
              print("홀수")

print()

b = input("정수 입력 : ")
last = b[-1]

if last in "02468":
    print("짝수")
if last in "13579":
    print("홀수")

c = input("정수 입력 : ")
c = int(c)
if c % 2 == 0:
    print("짝수")
if c % 2 != 0:
    print("홀수")
