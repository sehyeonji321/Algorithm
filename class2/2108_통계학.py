# mean / median / freq / range

def new_round(n): # 사실 n이 홀수이기때문에, 정수/홀수가 .5 형식으로 나올일은 없어서 그냥 round()를 써도 된다.
    if n >= 0:
        if n - int(n) >= 0.5:
            return int(n) + 1
        else:
            return int(n)
    else:
        if n - int(n) < -0.5:
            return int(n) -1
        else:
            return int(n)
    

def find_freq(nums): # 정렬된 리스트를 받음
    cnt_dict = {}
    for k in nums:
        if k in cnt_dict:
            cnt_dict[k] += 1
        else:
            cnt_dict[k] = 1

    # cnt가 젤 많은 key
    freqs = [key for key, val in cnt_dict.items() if max(cnt_dict.values()) == val]
    freqs = sorted(freqs)

    if len(freqs) >= 2:
        return freqs[1]
    else:
        return freqs[0]


N = int(input())
nums = [int(input()) for _ in range(N)]
nums = sorted(nums)

avg = new_round(sum(nums)/N)
median = nums[N//2]
freq = find_freq(nums)
ran = max(nums) - min(nums)

print(avg, median, freq, ran, sep="\n")


