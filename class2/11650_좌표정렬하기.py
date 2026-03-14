# # sort()를 쓰지 않고 구현해보자. (삽입정렬 기반) -> 시간초과!
# N = int(input())
# arr = []

# for _ in range(N):
#     x, y = map(int, input().split())
#     new_point = [x,y]

#     inserted = False
#     for k in range(len(arr)-1, -1, -1):
#         if arr[k][0] < x or (arr[k][0] == x and arr[k][1] < y):
#             arr.insert(k+1, new_point)
#             inserted = True
#             break

#     if not inserted:
#         arr.insert(0, new_point)

# for nums in arr:
#     print(nums[0], nums[1])


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

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0] or (left[i][0] == right[j][0] and left[i][1] < right[j][1]):
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

