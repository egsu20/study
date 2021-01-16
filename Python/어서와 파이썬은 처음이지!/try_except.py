# ZeroDivisionError
try:
    output = 150/0
except ZeroDivisionError as e:
    print(e)

# ValueError
try:
    n = input("정수를 입력하시오 : ")
    n = int(n)
except:
    print("정수가 아닙니다")

# IOError
try:
    fname = input("파일 이름 입력 : ")
    infile = open(fname, "r")
except IOError:
    print(fname+"이 없는 것 같습니다.")
