from collections import deque, defaultdict
import copy
INF = 10**9

def flow(f, c, pre, s, e):
    cur_f = INF
    i = e
    while i != s:
        cur_f = min(cur_f, c[pre[i]][i] - f[pre[i]][i])
        i = pre[i]
    i = e
    while i != s:
        f[pre[i]][i] += cur_f
        f[i][pre[i]] -= cur_f
        i = pre[i]
    return cur_f


def bfs(d, f, c, pre, s, e):
    p = copy.deepcopy(pre)
    queue = deque()
    queue.append(s)
    while queue:
        curr = queue.popleft()
        for next in d[curr]:
            if c[curr][next]-f[curr][next] > 0 and not p[next]:
                p[next] = curr
                queue.append(next)
                if next == e:
                    return flow(f, c, p, s, e)
    return 0


def EK(d, f, c, pre, s, e):
    ans = 0
    while 1:
        max_flow = bfs(d, f, c, pre, s, e)
        if max_flow > 0:
            ans += max_flow
        else:
            break
    return ans

if __name__ == '__main__':
    n = int(input())
    D = defaultdict(list)
    F = defaultdict(dict)
    C = defaultdict(dict)
    Pre = defaultdict(bool)

    for _ in range(n):
        p1, p2, v = input().split()
        v = int(v)
        D[p1].append(p2)
        D[p2].append(p1)
        F[p1][p2] = 0
        F[p2][p1] = 0
        if p2 in C[p1]:
            C[p1][p2] += v
        else:
            C[p1][p2] = v
        if p1 in C[p2]:
            C[p2][p1] += v
        else:
            C[p2][p1] = v
        Pre[p1] = False
        Pre[p2] = False

    print(EK(D,F,C,Pre,'A','Z'))
