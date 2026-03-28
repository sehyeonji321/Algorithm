# 우선 각각의 배추위치를 노드로 생각해서, 연결된 노드 세트가 몇개인지 알아봐야 할 듯 하다.
# 우선 그래프를 만든 다음, BFS같은걸 돌려서 연결된 노드세트를 구한 뒤, 이걸 정렬한다.
# 그 다음, 이 노드세트가 이미 기록되어있으면 추가로 저장하지 않고, 기록되어있지 않으면 추가로 저장한다.
# 위 과정을 반복한 뒤, 저장된 노드세트가 몇 개인지 구한다.
# 근데, 입력이 노드로 들어오는게아니라, 그냥 배추 좌표만 들어오기에 이게 연결된 노드인지 아닌지 구별하는 로직이 추가로 또 필요..

# 그냥 좌표를 입력받고, 좌표 하나가 노드 하나라고 생각하자.
# 이제 모든 좌표들을 순차적으로 검사한다. 만약 1이 발견되면(배추가 발견되면), 그 자리에서 BFS를 돌려서 인접 배추를 확인
# 배추들을 확인하며 모두 뽑아버린다. -> 다 돌았으면 지렁이 1개 추가.
# 위 과정을 반복하면 된다. 
# DFS를 하면, 재귀깊이 제한이 있을 수 있으니 BFS로 해보자.

from collections import deque
import sys
input = sys.stdin.readline



def bfs(graph, x, y, M, N): # 입력받은 좌표에서 시작하여, dfs로 배추 있는 곳을 돌면서 배추 뽑는 함수
    queue = deque([(x,y)]) # bfs 시작점
    graph[x][y] = 0 # 우선 해당 좌표의 배추를 뽑음

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue: # 큐가 빌 때 까지..
        x, y = queue.popleft()

        for k in range(4): # 상하좌우 순서대로 보면서
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 1: # 인근 좌표에 배추가 있다면
                    graph[nx][ny] = 0 # 배추를 뽑고
                    queue.append((nx, ny)) # 탐색 후보로 추가


T = int(input().rstrip())

for _ in range(T):
    M, N, K = map(int, input().split())
    
    # 배추밭 만들기
    graph = [[0 for _ in range(N)] for _ in range(M)]

    # 배추 심기 완료
    for k in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    
    result = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1: # 배추 발견하면
                bfs(graph, i,j, M, N) # 인근 배추 다 뽑아버림
                result += 1
    
    print(result)
            

    
