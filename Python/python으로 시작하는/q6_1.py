class You:
    def setname(self, n):
        self.name = n
    def setage(self, a):
        self.age = a
    def show(self):
        print('name :',self.name, 'age :', self.age)

my = You()
my.setname('준서')
my.setage(21)
my.show()
