arr = [0]*50001
arr[1] = 1

n = int(input())


for a in range(2, n+1):
    arr[a] = a
    i = 1
    while i * i <= a:
        arr[a] = min(arr[a], arr[a-i**2]+1)
        i += 1

print(arr[n])
