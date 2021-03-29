bird_pos = []
animals = ['새','코끼리', '강아지','새','강아지','새']

for i , animal in enumerate(animals):
    if(animal=='새'):
        bird_pos.append(i)

print(bird_pos)


animals = ['새', '코끼리', '강아지']
for i, animal in enumerate(animals):
    print(i, animal)

