while True:
    a, b, c = map(int, input().split())

    if a == b and b == c and a == 0:
        break

    a, b, c = sorted((a, b, c))

    if c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")