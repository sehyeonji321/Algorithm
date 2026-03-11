# 3의 배수는 3칸씩 띄엄띄엄 등장
# 따라서, 입력이 3개라면 이 중 하나는 무조건 숫자여야함을 이용하자.


for i in range(3):
    seq = input()
    
    # 숫자를 받는 순간, 어떤 숫자를 받았는지 + 언제 받았는지 기록하고 반복 종료
    if seq != "Fizz" and seq != "Buzz" and seq != "FizzBuzz":
        val = int(seq)
        idx = i
        break

# idx+1번째에 숫자 val이 나옴.
num = val + (3-idx)

# 원하는 형식으로 출력
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
