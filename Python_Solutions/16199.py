by, bm, bd = map(int, input().split())
dy, dm, dd = map(int, input().split())
age = 0
if dy > by:
    if dm > bm or (dm == bm and dd >= bd):
        age = dy-by
    else:
        age = dy-by-1
print(age)
print(dy-by+1)
print(dy-by)