N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# Method 1
# 전체길이 8 -> 완벽한 8by8이 있나? (0,1 케이스 나눠서) 
# 있다면 다 -1로 바꾸고, 0, 1 나눠서 카운트
# 완벽한 4by4행렬이 있나? -> 위와 같이.
# 반복

# Method 2 (분할정복)
# 주어진 N크기짜리 완벽한게 있나 확인
# 있으면 하나 세리고, 없다면 4등분해서 똑같이 확인
# 배열을 직접 잘라서 넣어주기보단, 배열은 그냥 전역변수인채로 쓰고(수정이 아니라 조회만하므로 괜찮)
# 대신, 시작점과 n을 입력으로 주면 간단하다.

def check_all(x, y, N, color):
    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[i][j] != color:
                return False
    return True

def check(x, y, N, counts): # white, blue처럼 int형으로 넣어주면, 재귀호출 시 immutable 객체라 변경불가 -> 배열을 넣자
    if check_all(x, y, N, 0):
        counts[0] += 1
        return
    elif check_all(x, y, N, 1):
        counts[1] += 1
        return
    
    # 가득차지 않은 경우
    next = N//2
    check(x, y , next, counts)
    check(x+next, y, next, counts)
    check(x, y+next, next, counts)
    check(x+next, y+next, next, counts)

    # 외부에 선언된 counts를 직접 변경한 경우이므로 별도로 counts를 다시 반환할 필요 없다.

counts = [0,0]
check(0,0,N,counts)
print(counts[0])
print(counts[1])