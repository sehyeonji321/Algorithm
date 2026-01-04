N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

T_nums = []
for n in size:
    if n % T == 0:
        T_nums.append(n // T)
    else:
        T_nums.append(n // T + 1)
T_sum = sum(T_nums)

p1 = N // P
p2 = N % P

print(T_sum)
print(p1, p2)