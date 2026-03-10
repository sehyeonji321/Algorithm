A, B, V = map(int, input().split())

if V <= A:
    print(1)
else:
    diff = (A-B)
    if (V-A) % diff == 0:
        print((V-A) // diff + 1)
    else:
        print(((V-A) // diff) + 2)


'''
아래 코드로 돌리면 시간 초과!
day = 1
h = 0
while True:
    h += A
    if h >= V:
        print(day)
        break
    h -= B
    day += 1
'''