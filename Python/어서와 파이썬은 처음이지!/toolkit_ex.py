# abs(x) : 절대값 반환
print(abs(-5))

# all(iterable) : and와 같은 역할
# iterable의 모든 요소가 참이면 참을 반환
def all(iterable):
    for element in iterable:
        if not element:
            return false
    return True

# any(iterable) : or과 같은 역할
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# bool(x) : x를 부울형으로. 0->False, 1->True
items = ["", "a string", 0, 1, [], []]
for i in items:
    print(i, bool(i))

# chr(x) : 아스키 코드값->문자
# ord(x) : 문자의 아스키 코드값
print(chr(65))
print(ord('A'))
