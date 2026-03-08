N, M = map(int, input().split())
cards = list(map(int, input().split()))

def find(M, cards):        
    while True:
        for i in range(0, N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    if M == cards[i]+cards[j]+cards[k]:
                        return M
        M = M-1        

print(find(M, cards))