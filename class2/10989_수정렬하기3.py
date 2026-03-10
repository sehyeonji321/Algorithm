'''
# 병합 정렬 구현 -> 비교기반 정렬이라, 메모리 초과.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 반 갈라서, 각각 병합정렬 후 합칠 것.
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return_arr = []

    # 병합정렬 된 두 배열을 합치는 과정
    while True:
        if len(left_arr) == 0:
            return_arr = return_arr + right_arr
            break
        if len(right_arr) == 0:
            return_arr = return_arr + left_arr
            break
        if left_arr[0] <= right_arr[0]:
            return_arr.append(left_arr[0])
            del(left_arr[0])
        else:
            return_arr.append(right_arr[0])
            del(right_arr[0])
        
    return return_arr
'''


N = int(input())

# 이 문제는 비교기반으로 직접 정렬하려면 메모리 초과가 생긴다.
# 수의 갯수가 1천만까지 가능하기 때문.. 따라서 비교기반이 아닌 counting sort를 쓰자!
# 배열을 실제로 "저장" 후 "정렬"할 필요가 없다.
# 출력을 하기 위해 필요한 정보는, 각 수가 얼마나 나왔는지 뿐!
arr = [0 for _ in range(10001)] # idx에, idx라는 "수"가 몇번 입력되었는지 기록

for _ in range(N):
    num = int(input())
    arr[num] += 1

for i in range(1,10001):
    for j in range(arr[i]):
        print(i)

