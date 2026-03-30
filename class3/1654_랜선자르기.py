import sys
input = sys.stdin.readline

K, N = map(int, input().split())

LAN = []
for _ in range(K):
    LAN.append(int(input().rstrip()))

# 이분탐색 기반.
# mid로 잘랐을 때, 원하는 개수보다 더 나오면 mid를 더 키워봐도 ok
# 원하는 개수만큼 안나온거면 너무 길게 자른 것.
start = 1
end = max(LAN)
ans = 0 # 이 문제에선 필요없긴하다. 무조건 답이 존재하기때문

while start <= end:
    mid = (start+end)//2
  
    total = 0
    for k in LAN:
        total += k//mid

    if total >= N: # 끝내도 되지만, 더 좋은 값이 있을 수 있다.
        ans = mid # 우선 정답 후보로 저장
        start = mid+1 # 다른 후보 탐색!
    else: # 현재 mid는 절대 답이 될 수 없다.
        end = mid-1

print(ans)
# 브루트포스가 젤 쉬워보이긴하지만, 시간초과
# i = 1
# while True:
#     total = 0
#     for k in LAN:
#         total += k//i
    
#     if total < N: # 처음으로 못만드는 순간이 온다.
#         break
#     i += 1

# print(i-1)