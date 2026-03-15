def check(seq):
    stack = []

    for s in seq:
        if s == "(":
            stack.append(0)
        elif s == "[":
            stack.append(1)
        elif s == ")":
            if len(stack) == 0:
                return False
            if stack.pop() != 0:
                return False
        elif s == "]":
            if len(stack) == 0:
                return False
            if stack.pop() != 1:
                return False
    if len(stack) == 0:
        return True
    



while True:
    seq = input()
    if seq == ".":
        break

    if check(seq):
        print("yes")
    else:
        print("no")
