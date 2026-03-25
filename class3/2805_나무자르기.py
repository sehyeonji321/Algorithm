import sys
input = sys.stdin.readline

def get_len(h, woods): # h 높이로 잘랐을 때 얻는 나무길이의 합 
    result = 0
    for k in woods:
        result += k-h if k-h > 0 else 0
    return result    

N, M = map(int, input().split())
woods = list(map(int, input().split()))

low = 0
high = max(woods)
res = 0

while low <= high:
    mid = (low+high)//2

    if get_len(mid, woods) >= M: # 일단은 조건은 만족. 더 높이 잘라도 되는지 확인해봐야함
        res = mid
        low = mid+1

    else:
        high = mid-1

print(res)


# # 지금 나무 길이가 너무 길 수도 있다. -> 1칸씩 내려가면서 찾으면 한참 걸림 -> Bianry search인듯?
# high = max(woods)
# while high >= 0:
#     if M == get_len(high, woods):
#         print(high)
#         break
#     high -= 1


