import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memo = {}

for _ in range(N):
    site, pw = input().split()
    memo[site] = pw

for _ in range(M):
    site = input().rstrip()
    print(memo[site])