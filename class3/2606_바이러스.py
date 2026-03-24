import sys
input = sys.stdin.readline

n_computer = int(input().rstrip())
adjacency = [[0 for _ in range(n_computer+1)] for _ in range(n_computer+1)] # 노드의 연결 상태를 기록하는 행렬

comb = int(input().rstrip())

for i in range(comb):
    a, b = map(int, input().split()) # 인접한 두 수를 받아, adj 행렬에 기록한다.
    adjacency[a][b] = 1
    adjacency[b][a] = 1

virus = []

# 주어진 node와 연결되어있는 모든 노드를 찾는 함수
# 1. 주어진 node와 직접적으로 연결되어있는 노드를 adj에서 뽑아서, 목록에 추가한다.
# 2. 해당 노드들과 연결된 노드를 뽑아 또 목록에 추가한다.
def find_adj(node):
    if node in virus:
        return
    virus.append(node)
    for k in range(1,n_computer+1):
        if adjacency[node][k] == 1:
            find_adj(k)

find_adj(1)
print(len(virus)-1)