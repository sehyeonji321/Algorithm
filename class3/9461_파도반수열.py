# 1 1 1 2 2 3 4 5 7 9 12 16 21 28 37 (37+12 = 49)
# a_n = a_(n-1) + a_(n-5) (n >= 6)임을 관찰할 수 있다.
# 수학으로 구현할 경우 -> 그냥 동차 점화식 풀면 ok
# 여기서는 DP로 풀어보자.


arr = [0]* 101
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2

for k in range(6,101):
    arr[k] = arr[k-1] + arr[k-5]

T = int(input())
for _ in range(T):
    n = int(input())
    print(arr[n])