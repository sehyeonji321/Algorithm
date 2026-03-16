def check(seq):
    stack = []
    mapping = {")": "(", "]":"["}

    for s in seq:
        if s == "(" or s == "[": # 여는 괄호면 스택에 넣음
            stack.append(s)
        elif s == ")" or s == "]": # 닫는 괄호면, pop할 수 없거나, 스택에서 뽑은게 쌍이 안맞으면 False
            if not stack or stack.pop() != mapping[s]:
                return False
    return len(stack) == 0
    
while True:
    seq = input()
    if seq == ".":
        break
    print("yes" if check(seq) else "no")