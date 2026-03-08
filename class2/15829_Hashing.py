L = int(input())
seq = list(input())
seq = list(map(ord, seq))

H = 0
r = 31
M = 1234567891

i = 0
for a in seq:
    H += (a-96)*(r**i)
    i += 1

print(H % M)
