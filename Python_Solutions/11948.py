s = 0; min1 = 100; min2 = 100
for _ in range(4):
    score = int(input())
    s += score
    if score < min1:
        min1 = score
for _ in range(2):
    score = int(input())
    s += score
    if score < min2:
        min2 = score
print(s-min1-min2)