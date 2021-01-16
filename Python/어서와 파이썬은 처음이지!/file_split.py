infile = open("proverbs.txt", "r")

for line in infile:
    line = line.rstrip() # 쥴바꿈 기호 삭제

    # 공백문자로 단어 분리
    # () 안에 ":"와 같이 분리 문자를 지정해 줄 수 있음
    word_list = line.split()

    for word in word_list:
        print(word)

infile.close()
