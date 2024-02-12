total = 0
for i in range(int(input())):
    q, y = map(float, input().split())
    total += q*y
print(f'{total:.4f}')