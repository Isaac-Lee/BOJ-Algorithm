n, m = map(int, input().split())
if 1 <= m <= 2:
    print('NEWBIE!')
elif m <= n:
    print('OLDBIE!')
else:
    print('TLE!')