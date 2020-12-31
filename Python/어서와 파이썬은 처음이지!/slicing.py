squares = [0,1,4,9,16,25,36,48]

print(squares[:3]) # [0:3]
print(squares[4:]) # [4:len(squares)]
print(squares[:]) # [0:len(squares)]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C','D','E']
print(letters)

letters[2:5] = []
print(letters)
