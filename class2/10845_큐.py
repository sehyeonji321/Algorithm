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

    def size(self):
        return self.length
    
    def empty(self):
        return 1 if self.length == 0 else 0
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[self.f]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[-1]
        

N = int(input())
q = queue()

for _ in range(N):
    line = input().split()
    cmd = line[0]

    if cmd == "push":
        q.push(int(line[1]))
    else:
        method = getattr(q, cmd) # q.cmd와 같다. string의 cmd를 가지고 함수처럼 실행가능! 스택문제에서의 q에대한 종속성이 없어짐
        print(method())