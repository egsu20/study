import keyword

input_a = input("변수 이름 입력 : ")

if keyword.iskeyword(input_a):
    print(input_a + "는(은) 예약어")
    print("--- 전체 키워드 ---")
    print(keyword.kwlist)

else:
    print(input_a + "은 사용가능한 변수 이름")
