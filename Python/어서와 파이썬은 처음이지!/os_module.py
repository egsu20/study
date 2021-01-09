# os의 기본적인 기능들을 다룰 수 있도록 해주는 모듈
import os

os.system("calc")

# 해당 경로의 파일과 디렉터리들의 리스트를 만들어 반환
print(os.listdir("."))


# mkdir() : 디렉터리 생성
os.mkdir("myfiles")
