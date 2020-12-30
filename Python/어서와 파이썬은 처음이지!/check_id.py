user_list = ['김철수', '홍길동', '김영희']

name = input("이름 : ")

if name in user_list:
    password = input("비밀번호 : ")
    if password == "1234":
        print("환영합니다.")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("알 수 없는 사용자")
