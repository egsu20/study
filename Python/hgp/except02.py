list_number = [234,12,53,45,122]

try:
    number_input = int(input("정수 입력 : "))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해 주세요")
except IndexError:
    print("인덱스 범위 벗어남")