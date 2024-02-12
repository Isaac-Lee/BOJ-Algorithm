color = {'R': 45,
         'G': 30,
         'B': 20,
         'Y': 15,
         'O': 10,
         'W': 5}
for _ in range(int(input())):
    price, d, c, p = input().split()
    price = float(price)*(100-color[d])/100
    if c == 'C':
        price *= 0.95
    if p == 'C':
        price = round(price, 1)
    print(f'${price:.2f}')
