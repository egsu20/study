table = []

rows = 10
cols = 10

for row in range(rows):
    table += [[0]*cols]

for row in range(rows):
    for col in range(cols):
        if (row+col)%2 == 0:
            table[row][col] = 1

for row in range(rows):
    for col in range(cols):
        print(table[row][col], end=" ")
    print()
