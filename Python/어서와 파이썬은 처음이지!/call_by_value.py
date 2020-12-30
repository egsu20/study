# 값에 의한 호출
def hbd(s):
    s += "To you"

# 리스트는 변경 가능 객체
def modify(li):
    li += [6,7]

msg = "Happy Birthday"
print(msg)
hbd(msg)
print(msg) # 변경 x
print()

ls = [1,2,3,4,5]
print(ls)
modify(ls)
print(ls) # 변경 o
