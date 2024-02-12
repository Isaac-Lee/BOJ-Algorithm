coin = []
for _ in range(int(input())):
    coin.append(input())
print(min(coin.count("0"), coin.count("1")))