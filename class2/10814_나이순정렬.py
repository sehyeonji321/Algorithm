N = int(input())

peoples = [list(input().split()) for _ in range(N)]

for age in range(1, 201):
    for a, n in peoples:
        if int(a) == age:
            print(int(a), n)
