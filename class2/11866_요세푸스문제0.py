class queue:
    def __init__(self):
        self.queue = []
        self.f = 0 # self.f라는 인덱스부터만 "큐"로 인정
        self.length = 0

    def push(self, X):
        self.queue.append(X) # insert 연산은, 원소들을 직접 옮겨야해서 무겁다
        self.length += 1

    def pop(self):
        if self.length > 0:
            n = self.queue[self.f]
            self.f += 1
            self.length -= 1
            return n
        else:
            return -1


N, K = map(int, input().split())
q = queue()
seq = []

for i in range(1, N+1):
    q.push(i)

while True:
    if len(seq) == N:
        break
    for _ in range(K-1):
        q.push(q.pop())
    seq.append(q.pop())

print(f"<{', '.join(map(str, seq))}>")