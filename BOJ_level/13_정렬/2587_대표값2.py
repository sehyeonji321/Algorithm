def selection_sort(arr): # 각 페이즈마다 최솟값을 찾아서, 해당페이즈에 해당하는 원소랑 바꿈
    for i in range(len(arr)-1): # 배열을 i번째부터 보기 시작하겠다.
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


nums = []
for _ in range(5):
    nums.append(int(input()))
selection_sort(nums)

print(sum(nums)//5)
print(nums[2])
