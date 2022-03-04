from collections import deque
def bfs(n, k):
    if n == k:
        return 0, [n]
    if n > k:
        return n-k, [i for i in range(n, k-1, -1)]
    visit = [0 for _ in range(100001)]
    queue = deque([(n, 0, [n])])
    while queue:
        node = queue.popleft()
        p = node[0]
        s = node[1]
        d = node[2]
        if p == k:
            return s, d
        visit[p] = 1
        if p * 2 <= 100000 and visit[p*2] == 0:
            queue.append((p * 2, s+1, d + [p*2]))
        if p + 1 <= 100000 and visit[p+1] == 0:
            queue.append((p + 1, s+1, d + [p+1]))
        if p - 1 >= 0 and visit[p-1] == 0:
            queue.append((p - 1, s+1, d + [p-1]))


if __name__ == '__main__':
    n, k = map(int, input().split())
    s, d = bfs(n, k)
    print(s)
    print(*d)