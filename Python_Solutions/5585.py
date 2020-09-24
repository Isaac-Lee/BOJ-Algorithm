n = int(input())
n = 1000-n
coin = 0
coin += n//500
n = n%500
coin += n//100
n = n%100
coin += n//50
n = n%50
coin += n//10
n = n%10
coin += n//5
n = n%5
coin += n//1
n = n%1

print(coin)