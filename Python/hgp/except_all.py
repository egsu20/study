list_number = [234,12,53,45,122]

try:
    number_input = int(input("정수 입력 : "))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
    asdf.adfadf() # 정의되지 않은 함수 사용
except ValueError as exception:
    print("정수를 입력해 주세요")
    print(type(exception), exception)
except IndexError as exception:
    print("인덱스 범위 벗어남")
    print(type(exception), exception) # 이외의 모든 예외 처리
except Exception as exception:
    print("미리 파악하지 못한 예외 발생")
    print(type(exception), exception)