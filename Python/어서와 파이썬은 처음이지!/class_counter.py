# Counter 클래스 정의
class Counter:
    # 생성자. 디폴트 값은 0
    def __init__(self, value=0):
        self.count = value
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count

# Counter 객체 생성
c = Counter()

c.reset()
c.increment() 
print("카운터 c의 값은 :", c.get())

a = Counter(10)
print("카운터 a의 값은 :", a.get())
