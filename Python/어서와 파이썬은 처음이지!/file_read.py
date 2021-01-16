# 파일 열기
infile = open("phones.txt", "r")

# 문자 18개 출력
s = infile.read(18)
print(s)

# 파일에서 한 줄 읽기
line = infile.readline()
while line != "":
    # 줄바꿈 기호 삭제
    line = line.rstrip()
    print(line)
    line = infile.readline()


# 파일 닫기
infile.close()
