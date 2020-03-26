N = int(input())
storeInfo = input()
storeInfo = list(storeInfo.split())
yhdrink = 2
drinkN = 0
for i in range(N):
    if yhdrink == 2 and storeInfo[i] == '0':
        drinkN += 1
        yhdrink = 0
    elif yhdrink == 0 and storeInfo[i] == '1':
        drinkN += 1
        yhdrink = 1
    elif yhdrink == 1 and storeInfo[i] == '2':
        drinkN += 1
        yhdrink = 2
print(drinkN)