import random
def passwd(length):
    pw= str()
    chars = 'abcdefghijklmnopqrstuvwxyz' + '0123456789'+'!@#$%^&*()'

    for _ in range(length):
        pw = pw+random.choice(chars)
    return pw

print(passwd(8))
