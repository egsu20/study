def input_value(list_x, number):
    print(number, "개의 정수를 입력하세요")
    for i in range(number):
        num = int(input("정수 입력 : "))
        list_x.append(num)

def output_value(list_x, number):
    for i in range(number):
        print(i, ":",list_x[i])

def sum_value(list_x, number):
    value = 0
    for i in range(number):
        value += list_x[i]
        print(list_x[i], end = ", ")
    print("총합 :", value)
    