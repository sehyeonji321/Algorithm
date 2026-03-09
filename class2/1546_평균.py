N = int(input())
scores = list(map(int, input().split()))

# 최댓값 찾는 알고리즘을 직접 만들어서 쓰자.
m = scores[0]
for i in range(N):
    if scores[i] > m:
        m = scores[i]

result = 100*(sum(scores)) / (m*N)
print(result)