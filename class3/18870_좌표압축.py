import sys
input = sys.stdin.readline

N = int(input())
origin_seq = list(map(int, input().split()))

nums = sorted(list(set(origin_seq))) # 중복 제거 후 정렬 -> 몇 번째로 작은지 뽑아내면 된다.
nums_idx = dict((v, i) for i, v in enumerate(nums))

for k in origin_seq:
    print(nums_idx[k], end=" ")
