# a_(n+1) = a_(n) + 6*n
def seq(n):
    a = 1
    for i in range(1, n):
        a = a + 6*i
    return a       

N = int(input())

i = 1
while True:
    if seq(i) >= N:
        print(i)
        break
    i += 1