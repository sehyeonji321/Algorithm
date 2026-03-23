# 이것도 DP로 접근해야할 것 같다.
import sys
input = sys.stdin.readline

N = int(input())

scores = [int(input().rstrip()) for _ in range(N)]
scores = [0] + scores

DP = [0 for _ in range(N+1)]
if N >= 2:
    DP[1] = scores[1]
    DP[2] = scores[1]+scores[2]
else:
    DP[1] = scores[1]
# k번째에 오려면 -> k-1번째나 k-2번째에서 점프
# k-2번째에서 오는거는 상관없는데, k-1번째에서 오려면, 그 전에 두칸 연속으로 k-1번째에 도달했으면 안됐음
# 다시 말해, k-1번째에 올땐, k-3번째에서 k-2번째를 거치지 않고 k-1번째로 왔어야 했다.
for k in range (3,N+1):
    DP[k] = max(DP[k-2]+scores[k] , DP[k-3]+scores[k-1]+scores[k])

print(DP[N])



''' 
# 너무 그리디하게 움직여서 틀린 코드. 반례: [10, 20, 15]
# 마지막계단의 바로전까지 최대 점수 or 마지막계단의 2칸 전까지 최대 점수 중 큰 것인데...
# 그냥 고를수는 없고, 마지막계단의 바로전 계단의 최대점수를 얻기위해, 마지막에 1칸을 두번 연속 올라갔으면 빼야함.
# 최대점수와 동시에, 마지막 계단에 두칸 연속 올라갔는지 판별하는 마킹이 필요하다.

import sys
input = sys.stdin.readline

N = int(input())

scores = [int(input().rstrip()) for _ in range(N)]
scores = [0] + scores 
score_marking = [[0,False] for _ in range(N+1)]

if N >=2:
    score_marking[1] = [scores[1], False]
    score_marking[2] = [scores[1]+scores[2], True] # True면, 도착때 2칸 연속 왔다는 것.

for idx in range(3, N+1):
    if score_marking[idx-1][1] == True:
        score_marking[idx] = [score_marking[idx-2][0]+scores[idx], False]
    else:
        if score_marking[idx-1][0] >= score_marking[idx-2][0]:
            score_marking[idx][0] = score_marking[idx-1][0]+scores[idx]
            score_marking[idx][1] = True
        else:
            score_marking[idx][0] = score_marking[idx-2][0]+scores[idx]

print(score_marking[N][0])
'''