import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_listen = set()
no_look = set()

for _ in range(N):
    no_listen.add(input().rstrip())
for _ in range(M):
    no_look.add(input().rstrip())

inter = sorted(list(no_listen & no_look))
print(len(inter))
print(*inter, sep="\n")