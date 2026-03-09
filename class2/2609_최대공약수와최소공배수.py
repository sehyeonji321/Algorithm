def gcd(a,b):
    if a < b:
        a, b = b, a

    while b != 0:
        r = a % b
        a = b
        b = r
    return a

A, B = map(int, input().split())
print(gcd(A,B))
print(A*B // gcd(A,B))