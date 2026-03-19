n = int(input())
seq = [int(input()) for _ in range(n)]
 
# 4 3 6 8 7 5 2 1
# 4 3 / 6 / 8 7 5 2 1 감소 부분수열을 찾는다.
# 1 2 3 4 (push) -> 4 3 (pop) -> 5 6 (push) -> 6 (pop) ->  7 8 (push) -> 8 7 5 2 1 (pop)
# 근데 이렇게하면, 감소 부분수열과 그 길이를 관리하는 로직을 따로 만들어야 함.

stack = []
result = [] # +,-
pt = 1
is_pos = True

for target in seq:
    while pt <= target: # target을 찾을 때 까지 push
        stack.append(pt)
        result.append('+')
        pt += 1
    
    # target과 스택의 맨 위가 같다면..
    if target == stack[-1]:
        stack.pop()
        result.append('-')
    else: # 위에서 안걸러지면, target이 스택 밑쪽에 깔려있다는 소리
        is_pos = False
        break

if is_pos:
    for k in result:
        print(k)
else:
    print("NO")