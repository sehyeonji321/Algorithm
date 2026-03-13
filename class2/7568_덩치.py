N = int(input())

# 각각 (몸무게, 키)와, 덩치 등수를 기록할 리스트
sizes = [list(map(int, input().split())) for _ in range(N)]
records = [1 for _ in range(N)]

for i in range(N): # 각 학생마다
    for w,h in sizes:
        if sizes[i][0] < w and sizes[i][1] < h: # 다른 모든 학생들과의 몸무게,키를 비교
            records[i] += 1
    print(records[i], end=" ")




