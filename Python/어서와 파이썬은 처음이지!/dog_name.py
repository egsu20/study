dogNames = []

while True:
    string = input("강아지의 이름을 입력(종료 - 엔터) : ")

    if string == '':
        break

    dogNames.append(string)

for name in dogNames:
    print(name, end=", ")
