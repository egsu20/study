class MyCounter(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    # 이터러블 객체 자신을 반환
    def __iter__(self):
        return self

    def __next__(self):
        # low는 high보다 작아야 함
        if self.low > self.high:
            raise StopIteration
        else:
            self.low += 1
            return self.low - 1

for i in [1,2,3,4,5]:
    print(i, end=", ")
print()

for char in "python":
    print(char, end=" ")
print()


# 1부터 10까지의 정수 출력
c = MyCounter(1, 10)
for i in c:
    print(i, end=' ')
