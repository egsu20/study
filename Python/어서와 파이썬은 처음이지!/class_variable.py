class Television:
    # 클래스 변수
    serialNumber = 0
    
    def __init__(self):
        # 클래스 변수에 접근
        Television.serialNumber += 1
        self.number = Television.serialNumber


tv1 = Television()
tv2 = Television()
print(Television.serialNumber)
print(tv1.serialNumber)
