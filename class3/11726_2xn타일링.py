# 피보나치의 냄새가..
# 마지막 타일이 세로인지, 가로인지에 따라 두 케이스가 생김 -> 2*(n-1)의 경우와 2*(n-2)의 경우를 고려하면 끝
# 출력조건을 잘 읽자..

n = int(input())

arr = [1]*(1001)
arr[2] = 2

if n <= 2:
    print(arr[n])
else:
    for k in range(3,n+1):
        arr[k] = arr[k-1] + arr[k-2]
    print(arr[n]%10007)
