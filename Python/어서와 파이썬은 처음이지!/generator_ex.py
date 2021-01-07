# 함수를 이용하여 이터러블 객체 생성
def myGenerator():
    yield 'first'
    yield 'second'
    yield 'third'
    
def myCounter(low, high):
    while low <= high:
        yield low
        low += 1
    

for word in myGenerator():
    print(word)

for i in myCounter(1, 10):
    print(i, end=' ')
 
