N, r, c = map(int,input().split())

pos =  {"LL": 0, "LR": 1, "RL":2, "RR":3} # 사각형 위치마다 번호를 매긴다

# 이제 이분 탐색을 N번 하면서 LR위치를 찾는다.
start_r = 0
start_c = 0
end_r = 2**N
end_c = 2**N
record = []
for i in range(N):
    mid_r = (start_r + end_r)//2
    mid_c = (start_c + end_c)//2

    if r < mid_r and c < mid_c:
        record.append("LL")
        end_r = mid_r
        end_c = mid_c

    elif r < mid_r and c >= mid_c:
        record.append("LR")
        end_r = mid_r
        start_c = mid_c
        
    elif r >= mid_r and c < mid_c:
        record.append("RL")
        start_r = mid_r
        end_c = mid_c

    else:
        record.append("RR")
        start_r = mid_r
        start_c = mid_c

# 각 loop에서 몇 번째 사각형인지 번역
result = []
for k in record:
    result.append(pos[k])

order = 0
for i, p in enumerate(result):
    order += (2**(2*(N-i))//4)*p

print(order)



# LR 위치를 먼저 찾는다. (행방향으로 반씩 자르면서 왼쪽인지 오른쪽인지 / 열방향으로도)
# 가령 RR /LR / LR이 나왔다면, 큰 정사각형부터 4등분해서 아래오른쪽 / 그안에서 위오른쪽 / 그안에서 위오른쪽
# RR -> (2^{2*N}/4)*pos 부터, (2^{2N}/4)*(pos+1) 미만
# LR -> (2^{2*(N-1)}/4)*pos를, (2^{2*N}/4)*pos 여기에 더함 -> 이어서..
