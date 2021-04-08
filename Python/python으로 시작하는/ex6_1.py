class You:
    name = '' # 생략 가능
    def setname(self, n):
        self.name = n
    def show(self):
        print('name :', self.name)

my = You()
my.setname('준서')
my.show()
