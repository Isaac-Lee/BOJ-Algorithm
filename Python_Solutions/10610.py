n = list(map(int, input()))
n.sort(reverse=True)
if sum(n)%3 == 0 and n[-1] == 0:
    n.sort(reverse=True)
    for i in n:
        print(i, end="")
else:
    print(-1)
