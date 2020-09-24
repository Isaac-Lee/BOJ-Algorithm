def price(arr, Max):
    for i in range(1, 7):
        n = arr.count(i)
        if n == 2:
            return 1000+i*100
        elif n == 3:
            return 10000+i*1000
    return 100*Max

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    Max = max(arr)
    print(price(arr, Max))