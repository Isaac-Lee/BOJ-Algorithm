# 재귀를 이용한 풀이법 O(2^N)
# def lis(arr):
#     if not arr:                         # 배열이 비어있는 경우
#         return 0
#     ret = 1                             # ret 초기화
#     for i in range(len(arr)):           # 수열의 처음값 설
#         nxt = []
#         for j in range(i+1, len(arr)):  # 다음수의 후보르 배열에 추
#             if arr[i] < arr[j]:
#                 nxt.append(arr[j])
#         ret = max(ret, 1 + lis(nxt))
#     return ret

# 동적계획법 O(N^2)
# def lis(arr, n):
#     N = n
#     cache = [-1] * N
#
#     def find(start):
#         if cache[start] != -1:
#             return cache[start]
#
#         ret = 1
#         for nxt in range(start + 1, N):
#             if arr[start] < arr[nxt]:
#                 ret = max(ret, find(nxt) + 1)
#
#         cache[start] = ret
#         return ret
#
#     return find(0)

# 이진탐색을 이용한 풀이
def lis(arr):
    # C[i] means smallest last number of lis subsequences whose length are i
    INF = float('inf')
    C = [INF] * (len(arr)+1)
    C[0] = -INF
    C[1] = arr[0]
    tmp_longest = 1

    # Find i that matches C[i-1] < n <= C[i]
    def search(lo, hi, n):
        if lo == hi:
            return lo
        elif lo + 1 == hi:
            return lo if C[lo] >= n else hi

        mid = (lo + hi) // 2
        if C[mid] == n:
            return mid
        elif C[mid] < n:
            return search(mid+1, hi, n)
        else:
            return search(lo, mid, n)


    for n in arr:
        if C[tmp_longest] < n:
            tmp_longest += 1
            C[tmp_longest] = n
        else:
            next_loc = search(0, tmp_longest, n)
            C[next_loc] = n

    return tmp_longest

n = int(input())
arr = list(map(int, input().split()))
print(lis(arr))