def new_round(n): # 파이썬은 내장 round()가 2.5같은걸 이상하게 반올림..
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

N = int(input()) # can be zero
rmv = new_round(0.15*N) # 이거 2.5같은거 이상하게 반올림하지않나..

nums = [int(input()) for _ in range(N)]
nums = sorted(nums)
seq = nums[rmv:N-rmv]

if N == 0:
    avg = 0
else:
    avg = new_round(sum(seq)/(N- 2*rmv))
print(avg)