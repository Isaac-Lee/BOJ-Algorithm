name = []
for i in range(int(input())):
    name.append(input())

incr = sorted(name)
decr = sorted(name, reverse=True)
if incr == name:
    print("INCREASING")
elif decr == name:
    print("DECREASING")
else:
    print("NEITHER")