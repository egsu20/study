class Calc:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2
    def calculate(self, op):
        if op == '+':
            print(self.a, '+', self.b, '=', self.a+self.b)
        elif op == '*':
            print(self.a, '*', self.b, '=', self.a*self.b)
            
num1 = int(input('num1 : '))
num2 = int(input('num2 : '))
obj = Calc(num1, num2)
obj.calculate('+')
obj.calculate('*')
