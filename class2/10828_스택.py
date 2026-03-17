class stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, X):
        self.stack.insert(self.length, X)
        self.length += 1

    def pop(self): # 리스트의 .pop() 메서드를 이용해도 되지만.. 너무 날먹인 것 같아서
        if self.length > 0:
            num = self.stack[self.length - 1]
            self.length -= 1
            return num
        else:
            return -1

    def size(self):
        return self.length

    def empty(self):
        return 1 if self.length == 0 else 0

    def top(self):
        if self.empty():
            return -1
        return self.stack[self.length-1]

N = int(input())
s = stack()
cmds = {
    "pop": s.pop,
    "size": s.size,
    "empty": s.empty,
    "top": s.top
}

for _ in range(N):
    line = input().split()
    cmd = line[0] # push의 경우 좀 다르니까

    if cmd == "push":
        s.push(int(line[1]))
    else:
        print(cmds[cmd]())