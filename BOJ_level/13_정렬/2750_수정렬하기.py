# # 직접 정렬 vs 카운팅 정렬

# # 카운팅 정렬
# N = int(input())
# num_list = [0 for _ in range(2001)]

# for _ in range(N):
#     num = int(input())
#     num_list[num+1000] += 1

# for i in range(2001):
#     for j in range(num_list[i]):
#         print(i-1000)



# O(n^2)정도 되는 정렬 (버블, 선택, 삽입 정렬)
# 선택 정렬만 구현
def selection_sort(arr): # 각 페이즈마다 최솟값을 찾아서, 해당페이즈에 해당하는 원소랑 바꿈
    for i in range(len(arr)-1): # 배열을 i번째부터 보기 시작하겠다.
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

N = int(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

selection_sort(num_list)

for k in num_list:
    print(k)

