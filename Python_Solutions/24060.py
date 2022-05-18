import math

global K
count = 0

def merge(low_arr, high_arr):
    global count
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            count += 1
            if count == K:
                print(low_arr[l])
                quit()
            merged_arr.append(low_arr[l])
            l += 1
        else:
            count += 1
            if count == K:
                print(high_arr[h])
                quit()
            merged_arr.append(high_arr[h])
            h += 1
    if l == len(low_arr):
        while h < len(high_arr):
            count += 1
            if count == K:
                print(high_arr[h])
                quit()
            merged_arr.append(high_arr[h])
            h += 1
    if h == len(high_arr):
        while l < len(low_arr):
            count += 1
            if count == K:
                print(low_arr[l])
                quit()
            merged_arr.append(low_arr[l])
            l += 1
    return merged_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = math.ceil(len(arr)/2)
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    merged_arr = merge(low_arr, high_arr)
    return merged_arr

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    merge_sort(A)
    if count < K:
        print(-1)
