def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    
    last = int(n ** (1/2))
    for i in range(2, last+1):
        if n % i == 0:
            return False
    else:
        return True

N = int(input())
nums = list(map(int, input().split()))

sum = 0
for n in nums:
    if is_prime(n) == True:
        sum += 1

print(sum)

