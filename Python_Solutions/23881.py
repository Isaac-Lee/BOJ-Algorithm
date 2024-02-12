def selection_sort(n, k, arr):
    count = 0
    for i in range(n-1, -1, -1):
        index = arr.index(max(arr[:i+1]))
        if index != i:
            count += 1
            tmp = arr[i]
            arr[i] = arr[index]
            arr[index] = tmp
            if count == k:
                print(arr[index], arr[i])
                return count
    print(-1)
    return count

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    selection_sort(n, k, arr)
