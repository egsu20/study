import time

now = time.localtime()

print("현재 시간은",time.asctime())

hour = now.tm_hour

# 시간
if hour < 12:
    print("Good morning")
elif hour < 15:
    print("Good afternoon")
elif hour < 20:
    print("Good evening")
else:
    print("Good night")     

