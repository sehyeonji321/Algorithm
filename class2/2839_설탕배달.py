# # DP의 냄새가..
# # N 킬로그램에 필요한 수는, N-3에 필요한 것과 N-5에 필요한 것중 작은 것에 1을 더한 것.

# N = int(input())

# arr = [-1 for i in range(5001)] # 적당히 case를 나누고 N까지만 해도되지만.. 그냥 다 만들자.
# arr[3] = arr[5] = 1

# for idx in range(6, N+1):
#     if arr[idx-3] < 0 and arr[idx-5] < 0:
#         arr[idx] = -1
#     elif arr[idx-3] < 0:
#         arr[idx] = arr[idx-5] + 1
#     elif arr[idx-5] < 0:
#         arr[idx] = arr[idx-3] + 1
#     else:
#         arr[idx] = min(arr[idx-3], arr[idx-5]) + 1    

# print(arr[N])

# 아래는 더 간단한 DP 풀이. 굳이 -1로 초기화할 필요가 없다

N = int(input())

arr = [float('inf') for i in range(5001)]

arr[3] = arr[5] = 1

for idx in range(6,N+1):
    arr[idx] = min(arr[idx-3], arr[idx-5]) + 1

print(arr[N] if arr[N] != float('inf') else -1)