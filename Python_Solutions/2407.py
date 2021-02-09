import math
fac = math.factorial
n, m = map(int, input().split())
print(fac(n) // (fac(n-m)*fac(m)))