# 실제로 단어를 정렬하고 출력하는 경우
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    result_arr = []

    while True:
        if len(left_arr) == 0:
            result_arr = result_arr + right_arr
            break
        elif len(right_arr) == 0:
            result_arr = result_arr + left_arr
            break
        elif len(left_arr[0]) < len(right_arr[0]):
            result_arr.append(left_arr[0])
            del(left_arr[0])
        elif len(left_arr[0]) > len(right_arr[0]):
            result_arr.append(right_arr[0])
            del(right_arr[0])
        elif len(left_arr[0]) == len(right_arr[0]):
            if left_arr[0] <= right_arr[0]:
                result_arr.append(left_arr[0])
                del(left_arr[0])
            else:
                result_arr.append(right_arr[0])
                del(right_arr[0])
    
    return result_arr

N = int(input())

words = []
for _ in range(N):
    words.append(input())

words = merge_sort(words)
printed = []

for word in words:
    if word in printed:
        continue
    print(word)
    printed.append(word)


'''
# 단어를 실제로 정렬하지 않고, 출력 시에만 그렇게 보이게 하는 경우
N = int(input())
words = [input() for i in range(N)]
words.sort() # 알파벳 순서는 여기서 맞춰두고,
is_print = []
m = max(map(len, words))

for i in range(1, m+1): # 여기서 길이가 짧은 것부터 출력하게한다.
  for idx in range(len(words)):
    if len(words[idx]) == i and words[idx] not in is_print:
      print(words[idx])
      is_print.append(words[idx])

'''