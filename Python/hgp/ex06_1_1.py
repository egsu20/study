numbers = [52, 273, 32, 103, 90, 10, 275]

print("# (1) 요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
number = 10000
try:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number))) # index() 함수는 리스트 내부에 값이 없을 때 예외를 발생시킴
except:
    print("- 리스트 내부에 없는 값")
print()

print("--- 정상 종료 ---")