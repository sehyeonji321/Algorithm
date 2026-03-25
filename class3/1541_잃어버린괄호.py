# 가령 28+77-25+33+21-10+2-3+45+7-25 라고 치면, -가 나올 때마다, 다음 -가 나오기 직전까지의 term을 묶어서 괄호치면 된다.
# 즉, 28+77-(25+33+21)-(10+2)-(3+45+7)-25
# 근데 여기서, 어디까지 괄호를 칠지.. 이런걸 생각하면 참 머리가 아픈데, 사실 -가 한번이라도 나오면 이후의 항은 모두 빼기로 바뀐다!
# 하지만 이걸 구현하려면 문자열을 다듬어야하므로.. 더 힘들다??

formula = input().split("-") # 28+75, 25+33+21, ...

total = 0
for idx in range(len(formula)):
    nums = list(map(int, formula[idx].split("+")))
    if idx == 0:
        total += sum(nums)
    else:
        total -= sum(nums)

print(total)

