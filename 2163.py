def chocoBBusher(n, m):
    l = n+m-2
    h = (n-1)*(m-1)
    return l+h


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    print(chocoBBusher(n, m))