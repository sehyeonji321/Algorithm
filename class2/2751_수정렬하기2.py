N = int(input())

nums = [0 for _ in range(2000001)]


for _ in range(N):
    num = int(input()) # "절댓값"이 1000000 이하인 "정수"
    
    num = num + 1000000
    nums[num] += 1
    

for idx in range(2000001):
    if nums[idx] == 1:
        print(idx - 1000000)
