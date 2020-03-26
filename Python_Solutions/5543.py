from itertools import product
burger = []
drink = []
for i in range(3):
    burger.append(int(input()))
for j in range(2):
    drink.append(int(input()))
cost = [sum(n)-50 for n in product(burger, drink)]
print(min(cost))