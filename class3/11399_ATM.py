# 260321이후 push!!
import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))

# 몇 개 case를 가지고 생각해보면, greedy하게 세우는게 젤 좋은 전략이 된다.
# 오래 걸리는 사람이 뒤에 설 수록, 피해보는 사람이 적어진다고 생각
times = sorted(times)

# times 벡터와 [N, N-1, ... , 1] 벡터를 내적하는게 젤 빠르긴함
min_time = 0
for i in range(N, 0, -1):
    min_time += i*times[N-i]
print(min_time)