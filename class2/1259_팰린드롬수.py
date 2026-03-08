# 이 문제는 문자열의 슬라이싱을 이용하면 훨씬 쉽다.
# 하지만 문제 의도 상, 그렇게 풀지는 말자.

while True:
    seq = input()
    if seq == '0':
        break
    
    i = 0
    j = len(seq) - 1
    while True:
        if i>=j:
            print('yes')
            break
        
        if seq[i] != seq[j]:
            print("no")
            break
        i += 1
        j -= 1        