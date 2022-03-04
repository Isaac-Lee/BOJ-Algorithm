p1, q1, p2, q2 = map(int, input().split())
area = p1*p2/q1/q2/2
print(1 if int(area) == area else 0)