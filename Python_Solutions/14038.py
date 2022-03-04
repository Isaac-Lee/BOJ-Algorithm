count = 0
for _ in range(6):
    if input() == "W":
        count += 1

if count > 4:
    print(1)
elif count > 2:
    print(2)
elif count > 0:
    print(3)
else:
    print(-1)