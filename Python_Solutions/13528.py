c = float(input())
l = int(input())
price = 0
for i in range(l):
    w,l = map(float, input().split())
    price += w*l*c
print(f'{price:.8f}')