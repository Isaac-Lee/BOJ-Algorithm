def solution(k, n, arr):
    high = arr[-1]
    low = 1

    while low <= high:
        mid = (low + high) // 2
        s = 0
        for i in arr:
            if i > mid:
                s += i - mid

        if s >= n:
            low = mid + 1
        else:
            high = mid - 1

    return high


if __name__ == "__main__":
    K, N = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(solution(K, N, arr))