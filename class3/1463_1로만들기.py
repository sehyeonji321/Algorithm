
# 아마 직접 3으로 나누고, 2로 나누고, 이러면 시간초과가 날 것 같다.
# 생각해보면, 29는, 28에대한 (최솟값 + 1)으로 나타낼 수 있다.
# 27은, 26과 9중 더 작은 대응값 + 1.
# 12는, 6, 4, 11 중 가장 작은 대응값 + 1
# 이런 식으로, 이전 값을 재활용하는 DP로 문제를 풀 수 있다고 생각해볼 수 있다.

# 1->0 / 2-> 1 / 3-> 1 / 4->2 /
N = int(input())

vals = [0 for _ in range(N+1)]
if N >= 3:
    vals[2] = 1
    vals[3] = 1
elif N == 2:
    vals[2] = 1

for idx in range(4,N+1):
    if (idx%2==0) and (idx%3==0):
        vals[idx] = min(vals[idx//2], vals[idx//3], vals[idx-1]) + 1
    elif (idx%2==0):
        vals[idx] = min(vals[idx//2], vals[idx-1]) + 1
    elif (idx%3==0):
        vals[idx] = min(vals[idx//3], vals[idx-1]) + 1
    else:
        vals[idx] = vals[idx-1] + 1

print(vals[N])
