class You:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def show(self):
        print('name :',self.name, ', age :', self.age)

my = You('jisu', 22)
my.show()
