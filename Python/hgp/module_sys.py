import sys

# 명령 매개변수 출력 (프로그램 실행 시 추가로 입력하는 값들)
print(sys.argv)
print("---")

# 컴퓨터 환경 관련 정보 출력
print("getwindowsversion() :", sys.getwindowsversion())
print("---")
print("copyright :", sys.copyright)
print("---")
print("version :", sys.version)

# 프로그램 강제 종료
sys.exit()