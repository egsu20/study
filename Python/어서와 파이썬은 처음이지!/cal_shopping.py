total = int(input("구입 금액을 입력하시오 : "))

print("지불 금액은 ",sep="")

if total > 100000:
    discount = total * 0.05
    print(str(total - discount),sep="")
else:
    print(str(total), sep-"")
print("입니다.")
