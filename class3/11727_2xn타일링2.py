n = int(input())

arr = [1]*1001
arr[2] = 3

if n <= 2:
    print(arr[n])
else:
    for k in range(3, n+1):
        arr[k] = arr[k-1] + 2*arr[k-2]
    print(arr[n]%10007)