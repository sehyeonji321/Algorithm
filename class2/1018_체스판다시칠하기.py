M, N = map(int, input().split())

board = [list(input()) for _ in range(M)] # 꼭 2차원으로 받아야하나 싶긴한데, 일단 이렇게하자.

# 시작점으로 올 수 있는 좌표는
# 0 ~ (M-8), 0 ~ (N-8)
# 총 (M-7)*(N-7)개의 case에 대하여 브루트포스 진행

least_num = 64
for row in range(0, M-7):
    for col in range(0, N-7): # 시작점을 바꿔가며
        cnt1 = 0 # B, W로 시작했을 때 각각 바꿔야할 수
        cnt2 = 0
        
        for start in ['B','W']:
            for m in range(0,8):
                for n in range(0,8): # 내부의 8*8을 돌면서
                    if start == 'B':
                        if (m+n)%2 == 0 and board[row+m][col+n] == 'W':
                            cnt1 += 1
                        elif (m+n)%2 == 1 and board[row+m][col+n] == 'B':
                            cnt1 += 1
                    else:
                        if (m+n)%2 == 0 and board[row+m][col+n] == 'B':
                            cnt2 += 1
                        elif (m+n)%2 == 1 and board[row+m][col+n] == 'W':
                            cnt2 += 1
        cnt = min(cnt1, cnt2)
        if cnt < least_num:
            least_num = cnt

print(least_num)