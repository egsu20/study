list_input = ["52","23","254","스파이","103"]

list_number = []

for item in list_input:
    try:
        float(item)
        list_number.append(item)
    except:
        pass # 반드시 작성되어야 하는 코드라면 pass 대신 raise NotImplementedError 

print("{} 내부에 있는 숫자는".format(list_input))
print("{}입니다".format(list_number))