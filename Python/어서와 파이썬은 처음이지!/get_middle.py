string = input("문자열을 입력하시오 : ")

n = len(string)
if n % 2 != 0:
    print("중앙글자는", string[n//2])
else:
    print("중앙글자는",string[n//2-1] , string[n//2])
