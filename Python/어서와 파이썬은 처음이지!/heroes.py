marvle_heroes = ["아이언맨", "블랙위도우", "헐크"]
dc_heroes = ["슈퍼맨", "배트맨", "원더우먼"]

heroes = marvle_heroes + dc_heroes
print(heroes)

print(marvle_heroes * 3)

marvle_heroes.insert(1,"스파이더맨")
print(marvle_heroes)
print()

if "원더우먼" in dc_heroes:
    print("원더우맨은 영웅", end=", ")
    print(dc_heroes.index("원더우먼"))
print()

heroes.pop(4)
print(heroes)
heroes.remove("슈퍼맨")
print(heroes)
