# 파일 객체 생성
outfile = open("phones.txt", "w")

# 데이터 저장
outfile.write("hong 010-1234-5678\n")
outfile.write("kim 010-1234-5679\n")
outfile.write("lee 010-1234-5680\n")
print("데이터 저장 완료")

# 파일 닫음
outfile.close()
