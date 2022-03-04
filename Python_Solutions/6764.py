d = []
for _ in range(4):
    d.append(int(input()))

if d.count(d[0]) == 4:
    print("Fish At Constant Depth")
elif sorted(d) == d:
    print("Fish Rising")
elif sorted(d, reverse=True) == d:
    print("Fish Diving")
else:
    print("No Fish")