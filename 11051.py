import math

def binoCoef(n, k):
    nFac = math.factorial(n)
    kFac = math.factorial(k)
    return nFac//(kFac*math.factorial(n-k))

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    # memo = [[0]*(k+1)]*(n+1)
    print(binoCoef(n, k)%100000007)