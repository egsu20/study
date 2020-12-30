import random

def create_password():
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    password =""

    for i in range(8):
        index = random.randrange(len(alpha))
        password += alpha[index]
    return password

print("A :", create_password())
print("B :", create_password())
print("C :", create_password())