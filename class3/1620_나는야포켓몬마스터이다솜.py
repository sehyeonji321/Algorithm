import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemons_idx = {input().rstrip():i for i in range(1,N+1)}
idx_pokemons = list(pokemons_idx.keys())
problems = [input().rstrip() for _ in range(M)]

for p in problems:
    try:
        # idx에 해당하는 pokemon을 찾기
        idx = int(p) - 1
        print(idx_pokemons[idx])
        
    except:
        # pokemon에 해당하는 idx찾기
        print(pokemons_idx[p])
