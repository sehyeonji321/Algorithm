# 그냥 괄호 쌍이 맞는지만 확인하면 된다.

def check(line):
    stack = []
    
    for s in line:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if not stack or stack.pop() != "(":
                return False
    
    return len(stack) == 0

N = int(input())
for _ in range(N):
    print("YES" if check(input()) else "NO")