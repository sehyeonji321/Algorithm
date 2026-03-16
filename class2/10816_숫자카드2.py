# 정직하게 리스트로 저장하고 리스트에서 찾으면 시간초과 하는 문제.
# 정렬 후 이분탐색을 하려하니, "여러 개"의 값을 찾기가 애매한 것 같은데..

N = int(input())
sanggeun = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

count_dict = {}
for num in sanggeun:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for target in find:
    if target in count_dict:
        print(count_dict[target], end=" ")
    else:
        print(0, end=" ")