nolisten = set()
nosee = set()

n, m = map(int, input().split())
for i in range(n):
    nolisten.add(input())
for i in range(m):
    nosee.add(input())
nolistennosee = list(nolisten.intersection(nosee))
print(len(nolistennosee))
nolistennosee.sort()
for name in nolistennosee:
    print(name)