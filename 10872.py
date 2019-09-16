n = int(input())
def pec(num):
    re=1
    for i in range(1,num+1):
        re *= i
    return re

print(pec(n))