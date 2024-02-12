d = [0 for i in range(117)]
d[1] = 1
d[2] = 1
d[3] = 1
for i in range(4, 117):
    d[i] = d[i-1] + d[i-3]

n = int(input())
print(d[n])