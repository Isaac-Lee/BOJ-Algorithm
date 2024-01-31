import sys
input = sys.stdin.readline
EPS = 1e-9
n = int(input())
cont = sorted([int(input()) for _ in range(n)])
trim = round(n*0.15+EPS)
if n == 0:
  print(0)
elif trim == 0:
  print(round(sum(cont)/n+EPS))
else:
  print(round(sum(cont[trim:-trim])/(n-(trim*2))+EPS))