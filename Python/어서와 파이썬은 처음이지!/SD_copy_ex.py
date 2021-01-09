import copy


# shallow copy
colors = ["red", "blue", "green"]
copy_color = colors

copy_color[0] = "white"

print(colors)
print(copy_color)

# deep copy
colors = ["red", "blue", "green"]
copy_color = copy.deepcopy(colors)

copy_color[0] = "white"

print(colors)
print(copy_color)
