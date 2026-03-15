# 리스트에서 del(arr[0])과 같은 방법으로 풀려면, 시간초과!

from collections import deque

N = int(input())

q = deque(range(1, N+1))

while len(q) > 1:
    q.popleft()

    if len(q) == 1:
        break

    top = q.popleft()
    q.append(top)

print(q[0])