import sys
from collections import deque

input = sys.stdin.readline

def setup_graph(n, edges):
    graph = [[] for _ in range(n+1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return graph

def bfs(graph, start, visited): # bfs로 노드들을 방문하며, 방문한 노드 갯수를 최종출력
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]: # v의 인접노드들
            if visited[i] == False: # 아직 방문 안했으면
                visited[i] = True # 방문하고
                queue.append(i) # 대기열에 추가

# 메인 루프
N,M = map(int, input().split())
edges = []

for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u,v))

graph = setup_graph(N, edges) # 그래프 만들기까지 완료

# 노드를 하나씩 순회하며, 해당 노드를 기점으로 BFS를 돌리면서 마주치는 모든 노드를 방문처리.
# BFS가 실행될 때 마다 counting

connected_num = 0
visited = [False] * (N+1)
for i in range(1,N+1): # 1~N번 노드를 순회
    if visited[i] == False: # 아직 방문 안했으면
        bfs(graph, i, visited) # 인접 노드는 모두 방문 처리
        connected_num += 1

print(connected_num)