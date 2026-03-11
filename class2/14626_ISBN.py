ISBN = list(input())

sum = 0
for i in range(12):
    if ISBN[i] != "*":
        ISBN[i] = int(ISBN[i])
        if i % 2 == 0:
            sum += ISBN[i]
        else:
            sum += 3*ISBN[i]
    else:
        if i % 2 == 0:
            weight = 1
        else:
            weight = 3
sum += int(ISBN[12])

# sum + weight*x = 0 (mod 10)
r = (-1)*sum % 10
if weight == 1:
    print(r)
else: # 3x = r (mod 10) => x = 7*r (mod 10) 잉여역수 이용!
    print(7*r % 10)