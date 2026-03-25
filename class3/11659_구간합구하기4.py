import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# arr = [0] + arr 하고싶지만, 다 미는게 너무 오래걸릴까봐 그냥 인덱스 조심해서 쓰기로


# 그때그때 반복문으로 더하면 너무 오래 걸릴 듯.
# S_n 리스트를 만들어놓고, 가령 1,3이 들어오면 S_3-S_0을 내보내는 식으로 구현하자.

S = [0]
for k in range(1,N+1):
    S.append(S[k-1]+arr[k-1]) # 이전항(지금까지의 총합) + 새로운 항을 기록
    
for _ in range(M):
    start, end = map(int, input().split())
    print(S[end] - S[start-1])

    