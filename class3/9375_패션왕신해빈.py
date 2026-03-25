import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n_clothes = int(input().rstrip())
    kinds = {}

    for _ in range(n_clothes):
        name, kind = input().split()

        if kind not in kinds:
            kinds[kind] = []
        kinds[kind].append(name)
    
    numbers = [len(arr) for arr in kinds.values()]

    # 이제 적당히 반복을 돌리면서 numbers의 숫자들을 조합해서 total에 더해야하는데, 무식하게 반복문 돌리면 어려울 수도?
    # 대신 수학적으로 접근하자.
    result = 1
    for k in numbers:
        result *= (k+1)
    result -= 1 # 아무것도 안입는 경우 제외
    print(result)

    

# A = [1,2,3,4]
# B = [1,2,3,4,5,6]
# C = [1,2,3]
# D = [1,2,3,4,5]
# 4,6,3,5 
# 모든 조합의 곱을 더하는 아이디어는 여러개가 있는데...
# 1. "안입는 것"을 하나의 경우로 생각하거나 / 2. (x+a)(x+b)(x+c) = x^3 + (a+b+c)x^2 + (ab+ac+bc)x + abc 임을 관찰해보자..
