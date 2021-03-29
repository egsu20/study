animal = 'elephant'

print(animal.count('e'))

# 찾기
print(animal.find('e'))
print(animal.find('ep'))
print(animal.rfind('e'))
print(animal.index('e'))
print(animal.startswith('el'))

# in
print('n' in animal)
print('an' in animal)
print('n' not in animal)

# 수정
ai = 'python program'
print(ai.replace('p','P'))
print(ai.lower())
print(ai.upper())
print(ai.swapcase())
print(ai.capitalize())

# 공백 처리
animal = ' elephant '
print(animal.lstrip())
print(animal.rstrip())
print(animal.strip())


