import sys
input = sys.stdin.readline
s = []
for _ in range(5):
    s.append(input())

for i in range(15):
    for j in range(5):
        if i < len(s[j])-1:
            print(s[j][i], end="")
