n, m, h, l = map(int, input().split())
print(min((m//l) * (h//l), n))