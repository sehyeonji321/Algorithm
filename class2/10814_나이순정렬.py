N = int(input())

peoples = [input().split() for _ in range(N)] # input().split()이 이미 list

for age in range(1, 201):
    for a, n in peoples:
        if int(a) == age:
            print(int(a), n)
