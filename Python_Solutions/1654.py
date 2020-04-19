def solution(n, arr):
    high = arr[0]
    low = 0
    result = 0

    while low <= high:
        mid = (high + low) // 2
        cnt = 0
        if mid == 0:
            return 1
        for val in arr:
            cnt += val//mid
            if cnt >= n and mid > result:
                result = mid
                break

        if cnt < n:
            high = mid - 1
        else:
            low = mid + 1

    return  result

if __name__ == "__main__":
    K, N = map(int,input().split())
    arr = []

    for _ in range(K):
        arr.append(int(input()))
    arr.sort(reverse = True)

    print(solution(N, arr))