n = [i for i in range(1, 31)]
for _ in range(28):
    n.remove(int(input()))
for i in sorted(n):
    print(i)
