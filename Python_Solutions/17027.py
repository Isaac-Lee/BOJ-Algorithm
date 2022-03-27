def num_correct(start):
    current = start
    correct = 0
    for i in range(n):
        if current == A[i]: current = B[i]
        elif current == B[i]: current = A[i]
        if current == G[i]: correct += 1
    return correct
n = int(input())
A,B,G = [], [], []
for _ in range(n):
    a,b,g=map(int,input().split())
    A.append(a); B.append(b); G.append(g)
best = 0
for i in range(1, 4):
    best = max(best, num_correct(i))
print(best)