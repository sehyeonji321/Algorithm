import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
    arr.append(int(input().rstrip()))

# 병합 정렬을 구현해보자!
# 배열을 반으로 쪼개어서 -> 각각이 정렬되었다 치고 -> 그걸 예쁘게 합친다.
def merge_sort(arr):
    # 재귀 종료 조건
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    result.extend(left_arr[i:])
    result.extend(right_arr[j:])
        
    return result

new_arr = merge_sort(arr)
print(*new_arr, sep="\n")