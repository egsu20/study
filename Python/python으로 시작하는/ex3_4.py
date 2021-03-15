price = int(input('상품의 가격 : '))

expensive = price > 20000

# expensive는 bool 타입
if expensive:
    shipping_cost = 0
else:
    shipping_cost = 3000

print('배송비 :', shipping_cost)
