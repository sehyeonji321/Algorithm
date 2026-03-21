# 배수 조건이 왜 있을지? -> 큰 거부터 꽉 채우는 전략을 위한 필요조건
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(N)]

pt = 0
while True:
    if pt == N or coins[pt] > K: # 여기서 coins[pt]를 먼저 검사하면 indexError가 생길 수 있으므로 순서에 유의
        break
    pt += 1

cnt = 0
# 이제 pt-1부터 내려가면서 보면 ok
for i in range(pt-1, -1, -1):
    cnt += K//coins[i]
    K = K%coins[i]

    if K == 0:
        break

print(cnt)