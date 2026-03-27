import sys
from collections import deque
input = sys.stdin.readline


def set_graph(n, edges): # 노드 개수 / 연결된 간선 목록
    graph = [[] for _ in range(n+1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1,n+1):
        graph[i].sort()
    
    return graph


def dfs(graph, v, visited): # 재귀 기반 dfs. 현재 graph에서 v라는 노드에 도착한 상황을 본다.
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]: # 인접한 노드를 보는데,
        if visited[i] == False: # 방문한 적 없다면
            dfs(graph, i, visited) # visited 마킹은 dfs 들어가서 할거니까 안해도 된다?


def bfs(graph, start, visited ):
    queue = deque([start]) # start라는 노드에서 시작!
    visited[start] = True

    while queue: # queue가 빌 때 까지..
        v = queue.popleft() # 출력대기열에 있는 노드 v를 뽑아서
        print(v, end=" ") # v를 출력하고

        for i in graph[v]: # v 근방의 노드들도 큐에 추가
            if visited[i] == False: # 방문한적 없다면
                visited[i] = True # 우선 방문하고,
                queue.append(i) # 출력대기열에 추가


N, M, V = map(int, input().split()) # 노드 개수 / 간선 개수 / 시작 노드

edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append([u,v]) # 어차피 graph 만들 때, 반대방향도 추가할거라 [v,u]는 추가할필요 x

graph = set_graph(N, edges)

visited = [False] * (N+1)
dfs(graph, V, visited)

print()

visited = [False] * (N+1)
bfs(graph, V, visited)