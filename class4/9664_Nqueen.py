# 백트래킹의 냄새가...
N = int(input())
position = [0]*N # 각 행의 '몇 번째 column에' 퀸을 둘 것인가?

# 0. 각 row마다, 몇 번째 col에 퀸을 둬야하는지 고민해야하는 상황
# 1. 이전은 어떻게 잘 놔뒀고, 지금 k번째를 보는상황이라 치자
# 2. 만약 이전꺼랑 같은열에 있거나(중복), 대각선에 있으면(거리에따른..) 돌아간다.

def check(row): # row 행에 퀸을 문제 없이 놓았는지 검사
    for i in range(0, row):
        if position[row] == position[i]:
            return False
        if row - i == abs(position[row]-position[i]):
            return False
    return True


def n_queen(row): # row번째 행에 설치할 차례
    if row == N: # row 다 채움
        return 1
    
    # 현재 row에서, 유효한 정답이 몇개 파생되는지?
    local_cnt = 0
    for i in range(N):
        position[row] = i # i번째 column에다가 퀸을 놓아봄. 근데 외부에서 어떻게 position을 가져온거지
        if check(row): # row까지 괜찮나?
            local_cnt += n_queen(row+1)

    return local_cnt # 최종 return

cnt = n_queen(0)
print(cnt)