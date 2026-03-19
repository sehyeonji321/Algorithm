from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # 문서 갯수, 궁금한 문서의 현위치
    importance = list(map(int, input().split()))
    importance = deque(importance)
    importance[M] = str(importance[M]) # 궁금한 문서는 string으로 마킹한다.

    cnt = 0
    while True:
        for c in importance:
            if int(c) > int(importance[0]):
                tmp = importance.popleft()
                importance.append(tmp)
                break
        else:
            cnt += 1
            tmp = importance.popleft()
            if type(tmp) == str:
                print(cnt)
                break



'''
from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # enumerate를 써서 (인덱스, 중요도) 묶음으로 큐 생성
    # 예: [(0, 1), (1, 1), (2, 9), (3, 1), (4, 1), (5, 1)]
    importance = deque([(i, val) for i, val in enumerate(map(int, input().split()))])
    
    cnt = 0
    while True:
        # 큐에서 가장 높은 중요도를 찾음 (튜플의 두 번째 값(x[1]) 기준)
        max_imp = max(importance, key=lambda x: x[1])[1]
        
        current = importance.popleft()
        
        # 현재 문서의 중요도가 가장 높다면 인쇄
        if current[1] == max_imp:
            cnt += 1
            if current[0] == M: # 내가 찾던 그 문서(인덱스)가 맞다면 종료
                print(cnt)
                break
        else:
            # 더 높은 중요도가 있다면 뒤로 보냄
            importance.append(current)
'''


    