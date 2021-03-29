import random

print(random.random())
print(random.randrange(1,6)) # 1~5
print(random.randint(1,6)) # 1~6

chars = '한글우수'
print(random.choice(chars))

chars = ['한','글','우','수']
print(random.choice(chars))

print(chars)
random.shuffle(chars)
print(chars)
