# def is_destruction(num): # 입력으로 수가 아닌 "문자열"을 받아야한다.
#     nums = list(num)

#     cnt = 0
#     destruction = False

#     for n in nums:
#         if n == "6":
#             cnt += 1
#         else:
#             cnt = 0
        
#         if cnt == 3:
#             destruction = True
#             break
    
#     if destruction:
#         return True
#     else:
#         return False
    
# N = int(input())
# count = 0
# n = 666

# while True:
#     if is_destruction(str(n)):
#         count += 1
#     if count == N:
#         print(n)
#         break
#     n += 1
    

# 사실 파이썬의 in을 이용하면 훨씬 쉽게 풀 수 있다.

N = int(input())
n = 666
cnt = 0

while True:
    if "666" in str(n):
        cnt += 1
    if cnt == N:
        break
    n += 1

print(n)