nums = [[0 for _ in range(15)] for  _ in range(15)] # 15 by 15 행렬

for i in range(1, 15):
    nums[0][i] = i
for j in range(15):
    nums[j][1] = 1
for i in range(1, 15):
    for j in range(2,15):
        nums[i][j] = nums[i][j-1] + nums[i-1][j]

# 메인 루프
N = int(input())

for _ in range(N):
    k = int(input())
    n = int(input())
    print(nums[k][n])


# 가장 효율적인 구현은, (k,n) tuple을 모두 받아두고,
# 가장 오른쪽 윗집까지 배열을 구현해놓고, 한꺼번에 처리하는 것.
# 즉, (k,n)이 들어올때마다 처리하려고하면, 처음부터 다시 배열을 만드는 상황이 생기니까..
# -> 원래같으면 이렇지만, 다행히 k,n의 size가 1~14로 restrict 되어있다!