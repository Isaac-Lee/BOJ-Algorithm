w = 1
score = 0
for i in range(5):
    s = sum(map(int,input().split()))
    if s > score:
        w = i+1
        score = s
print(w, score)