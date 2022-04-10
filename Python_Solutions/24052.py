def insertion_sort(arr, n, k):
    count = 0
    for i in range(1, n):
        loc = i-1
        newItem = arr[i]
        while 0 <= loc and newItem < arr[loc]:
            arr[loc+1] = arr[loc]
            loc-=1
            count += 1
            if count == k:
                print(*arr)
                return count
        if loc+1 != i:
            arr[loc+1] = newItem
            count += 1
            if count == k:
                print(*arr)
                return count
    print(-1)
    return count

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    insertion_sort(arr, n, k)