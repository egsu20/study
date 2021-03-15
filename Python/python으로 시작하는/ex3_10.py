price = int(input("정가를 입력하시오 : "))


if price >= 100:
    total = price * 0.85
    print("10층에서 사은품을 받아가세요")
else:
    total = 0.90

print("할인된 상품의 가격 :", total)
