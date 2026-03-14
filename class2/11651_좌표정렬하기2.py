# sort()를 쓰지 않고, 병합정렬 기반으로 구현해보자. -> 통과!

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    # 병합하는 부분
    return merge(left_arr, right_arr)

def merge(left, right): # 두 배열의 순서를 비교해 병합하는 함수
    result = []
    i = j = 0

    while i < len(left) and j < len(right): # 11650 문제에서, 아래 부분만 바꾸면 ok
        if left[i][1] < right[j][1] or (left[i][1] == right[j][1] and left[i][0] < right[j][0]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 배열 다 합치기 (i, j중 끝까지 본 배열은 아무것도 합쳐지지 않는다.)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

N = int(input())
pts = [list(map(int, input().split())) for _ in range(N)]
pts = merge_sort(pts)
for nums in pts:
    print(nums[0], nums[1])