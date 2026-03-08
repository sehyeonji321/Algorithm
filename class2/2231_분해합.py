def get_factor(n):
    s = n
    while n != 0:
        s += n % 10
        n = n // 10
    return s

N = int(input())

for i in range(1, N):
    if get_factor(i) == N:
        print(i)
        break
else:
    print(0)