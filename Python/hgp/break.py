count = 0

while True:
    print("{}번째 반복문입니다.".format(count))
    contin = input("> 종료하시겠습니까?(y/n):")
    if contin in ["Y","y"]:
        break
    elif contin in ["N","n"]: 
        count+=1
        continue
    else:
        print("error")
