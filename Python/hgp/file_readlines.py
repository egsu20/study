with open("info.txt","r") as file:
    for line in file:
        # 변수 선언
    (name, weight, height) = line.strip().split(", ")

    if (not name) or (not height) or (not weight):
        continue

    bmi = int(weight) / ((int(height)/100)**2)
    result = ""
    if 25 <= bmi:
        result = "over"
    elif bmi 18.5 <= bmi:
        result = "avg"
    else:
        result = "under"

    print("\n".join([
        "{}",
        "{}",
        "{}"
    ]).format(name,height, weight))