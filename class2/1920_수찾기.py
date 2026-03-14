N = int(input())
A = set(map(int, input().split())) # 검색이 더 편한가?

M = int(input())
B = list(map(int, input().split()))

for num in B:
    if num in A:
        print(1)
    else:
        print(0)