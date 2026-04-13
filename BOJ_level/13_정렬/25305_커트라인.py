def selection_sort(arr): # 이번엔 내림차순으로
    for i in range(len(arr)-1):
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

N, k = map(int, input().split())
arr = list(map(int, input().split()))
selection_sort(arr)
print(arr[k-1])