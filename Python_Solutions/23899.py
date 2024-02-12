def selection_sort(n, arr, target):
    if arr == target:
        print(1)
        return
    for i in range(n-1, -1, -1):
        index = arr.index(max(arr[:i+1]))
        if index != i:
            tmp = arr[i]
            arr[i] = arr[index]
            arr[index] = tmp
            if arr == target:
                print(1)
                return
    print(0)
    return

if __name__ == '__main__':
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    selection_sort(n, arr_a, arr_b)
