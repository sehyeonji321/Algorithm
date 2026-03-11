N, K = map(int, input().split())

num = 1
denom = 1
for i in range(K):
    num *= (N-i)
for j in range(1,K+1):
    denom *= j

print(num//denom)