# 생성
s1 = str("hello") # str 생성자 호출
s2 = "hello" # 문자열 리터럴

# 문자열 단어 분리
s = "Mississippi"
print(s.split("i"))

# 부분 문자열 검색
s = input("파이선 소스 파일 이름 : ")
if s.endswith(".py"):
    print("올바른 파일 이름임")
else:
    print("올바른 파일 이름이 아님")

# 공백 문자 제거
s = " Hello"
print(s.strip())
