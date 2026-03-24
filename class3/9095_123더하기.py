import sys
input = sys.stdin.readline

T = int(input())


# 7을 1,2,3으로 나타내는 방법?
# 마지막에 더해지는 수는 1,2,3중 하나이다.
# 6을 나타내고 +1 / 5를 나타내고+2 / 4를나타내고+3
# 조합으로 치면 겹치는 경우가 생기지만, "순서"까지 고려하기 때문에 위의 경우는 겹치지 않음
# 즉, DP[7] = DP[6] + DP[5] + DP[4]
DP = [0 for _ in range(11)] # input이 10까지만 들어오므로
DP[1] = 1
DP[2] = 2
DP[3] = 4
for k in range(4,11):
    DP[k] = DP[k-1] + DP[k-2] + DP[k-3]

for _ in range(T):
    n = int(input().rstrip())
    print(DP[n])
