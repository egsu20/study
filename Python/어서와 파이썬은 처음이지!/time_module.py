import time

def fib(n):
    f = [0, 1]

    i = 2
    while True:
        f.append(f[i-1] + f[i-2])
        if f[i] > n:
            print()
            return;
        print(f[i], end = ' ')
        i += 1

# 1970년부터 현재까지의 절대시간
print(time.time())

# 피보나치 수열 계산 시간 측정
start = time.time()

fib(1000)

end = time.time()

print(end-start)

# 현재 날짜와 시간을 문자열로 표시
print(time.asctime())

t = (2021, 1, 9, 10, 55, 30, 0, 5, 0)
print(time.asctime(t))

# 현재 날짜와 시간을 튜플 객체로 반환
local_time = time.localtime()
year = local_time[0]
month = local_time[1]
day = local_time[2]
print(year, month, day)

# 지정된 초만큼 정지
for i in range(10, 0, -1):
    print(i, end=" ")
    time.sleep(1)
print("발사")
