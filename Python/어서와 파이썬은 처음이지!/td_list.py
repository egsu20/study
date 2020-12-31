# 생성
rows = 3
cols = 5

s = []

for row in range(rows):
    s += [[0] * cols]
# s += [([0]*cols) for row in range(rows)]

print(s)

# 겁근
rows = len(s)
cols = len(s[0])

for r in range(rows):
    for c in range(cols):
        print(s[r][c], end=", ")
    print()


