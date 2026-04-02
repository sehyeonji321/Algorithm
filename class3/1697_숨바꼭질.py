from collections import deque

def bfs(graph, start, visited, K):
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        v = queue.popleft()

        # 인접 노드 조사
        if 1 <= v < 100000:
            graph[v].append(v-1)
            graph[v].append(v+1)
            if 2*v <= 100000:
                graph[v].append(2*v)
        elif v == 0:
            graph[v].append(2*v)
            graph[v].append(v+1)
        else: # v = 100000
            graph[v].append(v-1)

        for k in graph[v]: # v의 인접 노드에 대해
            if visited[k] == -1: # 방문 안했으면
                visited[k] = visited[v] + 1 # 현재노드보다 오래 걸려서 첫방문.
                queue.append(k)
        
        if visited[K] != -1:
            break


N, K = map(int, input().split())

graph = [[] for _ in range(100001)] # 0 ~ 100000
visited = [-1] * 100001

bfs(graph, N, visited, K) 
print(visited[K])






'''
# 아래 코드는, edges를 미리 메모리에 모두 할당해야하기에 비효율적. 특정 노드에 도착하면 그때그때 계산하자.
# 예외 처리는 직접 하는게 직관적
edges.append((0,0))
edges.append((0,1))
edges.append((1,2))
edges.append((100000,99999))

for k in range(2, 100000):
    edges.append((k,k+1))
    edges.append((k,k-1))
    if 2*k <= 100000:
        edges.append((k, 2*k))
'''