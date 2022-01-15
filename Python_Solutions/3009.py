x_cor = {}
y_cor = {}

for _ in range(3):
    x, y = map(int, input().split())

    if x not in x_cor:
        x_cor[x] = 1
    else:
        x_cor[x] += 1

    if y not in y_cor:
        y_cor[y] = 1
    else:
        y_cor[y] += 1

fourth_cor = ""
for k in x_cor:
    if x_cor[k] == 1:
        fourth_cor += f"{k} "
for k in y_cor:
    if y_cor[k] == 1:
        fourth_cor += f"{k}"
print(fourth_cor)