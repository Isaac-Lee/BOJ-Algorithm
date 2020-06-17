n = int(input())
pattern = list(input())
l = len(pattern)
for i in range(n-1):
    s = list(input())
    for k in range(l):
        if s[k] != pattern[k]:
            pattern[k] = "?"
for c in pattern:
    print(c, end="")