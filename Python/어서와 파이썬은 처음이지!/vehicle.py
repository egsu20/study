class Vehicle:
    def __init__(self, make, model, color, price):
        self.make = make # 제조사
        self.model = model # 모델
        self.color = color # 차 색상
        self.price = price # 가격

    def set_make(self, make):
        self.make = make

    def get_make(self):
        return self.make

    def get_desc(self, a=""):
        return "차량 = ("+str(self.make)+","+\
               str(self.model)+","+\
               str(self.color)+","+\
               str(self.price)+","+\
               str(a)+")"

# 상속
class Truck(Vehicle):
    # Truck의 생성자
    def __init__(self, make, model, color, price, payload):
        # Vehicle의 생성자를 호출
        super().__init__(make, model, color, price)
        self.payload = payload # 적재 용량

    def set_payload(self, payload):
        self.payload = payload

    def get_payload(self):
        return self.payload

    def get_desc(self):
        return super().get_desc(self.payload)

truck = Truck("Tes", "Models S", "white", 1000, 2000)

truck.set_make("Tesla")
truck.set_payload(3000)
print(truck.get_desc())
