from datetime import datetime, timedelta
n, c = map(int, input().split())
t = datetime(1,1,1)
for i in range(n):
    s = input()
    t += timedelta(minutes=int(s[0]))
    if i > 0: t += timedelta(seconds=int(s[2:])-c)
    else: t += timedelta(seconds=int(s[2:]))

print(t.strftime('%H:%M:%S'))
