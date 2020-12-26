import datetime

now = datetime.datetime.now()

if now.hour<12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

if now.hour>12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

print()

if 3 <= now.month <= 5:
    print("{}, spring".format(now.month))

if 6 <= now.month <= 8:
    print("{}, summer".format(now.month))

if 9 <= now.month <= 11:
    print("{}, far".format(now.month))

if 12 == now.month or 1 <= now.month <= 2:
    print("{}, winter".format(now.month))