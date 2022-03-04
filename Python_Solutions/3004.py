n = int(input())
total = 2
add = 2
for i in range(1,n):
    total += add
    if i%2==0:
        add += 1
print(total)