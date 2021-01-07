class FibIterator:
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.maxValue = maxValue

    # 객체 자신을 반환하는 메소드
    def __iter__(self):
        return self

    # 다음 반복을 위한 값 반환
    # 피보나치 : fib(i) = fib(i-1) + fib(i-2)
    def __next__(self):
        # 전단계와 전전단계 더하기
        n = self.a + self.b

        # 더 이상의 값이 없음
        if n > self.maxValue:
            raise StopIteration()

        # 전전단계를 전단계로, 전단계를 새로운 값으로 변
        self.a = self.b
        self.b = self.n
        return n

# FibIterator 객체를 생성할 때 생성자의 매개변수로
# 아무런 값을 넘겨주지 않았으므로
# 객체에서 a=1, b=0, maxValue=50으로 설정
for i in FibIterator():
    print(i, end=" ")
