import sys
input = sys.stdin.readline # input()의 시간초과를 방지하기 위함

class sett:
    def __init__(self):
        self.s = {} # 해시 기반의 딕셔너리를 이용해 구현 -> 탐색이 리스트보다 빠르다.

    def add(self, x):
        if x not in self.s:
            self.s[x] = None

    def remove(self, x):
        if x in self.s:
            del self.s[x]

    def check(self, x):
        if x in self.s: # keys()를 꼭 안붙여도 ok
            return 1
        else:
            return 0
        
    def toggle(self, x):
        if x in self.s:
            self.remove(x)
        else:
            self.add(x)

    def all(self):
        self.s = {i:None for i in range(1,21)}
    
    def empty(self):
        self.s = dict([])


M = int(input())
s = sett()


for _ in range(M):        
    cmds = input().split()
    cmd = cmds[0]
    method = getattr(s, cmd)

    if cmd == "all" or cmd == "empty":
        method()
    elif cmd != "check":
        method(int(cmds[1]))
    else:
        print(method(int(cmds[1])))