# 수의 종류가 많지 않기에, 수를 따로 저장하지 않고 갯수만 저장해두는 카운팅 정렬이 좋음
import sys
input = sys.stdin.readline

arr = [0 for _ in range(10001)]
N = int(input().rstrip())

for _ in range(N):
    num = int(input().rstrip())
    arr[num] += 1

for k in range(1,10001):
    for i in range(arr[k]):
        print(k)
