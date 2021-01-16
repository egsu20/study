infile = open("test.txt", "r+")

string = infile.read(10)
print("읽은 문자열 :", string)

# 현재 읽기/쓰기 동작의 위치
position = infile.tell()
print("현재 위치 : ", position)

# 파일의 처음으로
position = infile.seek(0, 0)
string = infile.read(10)
print("다시 읽은 문자열 :", string)

infile.close()
