from animal import dog # animal 패키지의 dog 모듈
from animal import cat # animal 패키지의 cat 모듈

d = dog.Dog() # instance
d.hi()

c = cat.Cat()
c.hi()

# from animal import * : animal 패키지의 모듈을 전부 불러옴
# d = Dig()  d.hi()바로 가능

