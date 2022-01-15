total = [0,0,0,0,0]

for i in range(4):
    off, on = map(int, input().split())
    total[i+1] = total[i]-off+on

print(max(total))