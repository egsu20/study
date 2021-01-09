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
