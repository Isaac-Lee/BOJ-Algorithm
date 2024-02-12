import sys
import heapq

t = int(input())
for _ in range(t):
    min_q = []
    max_q = []
    num = {}
    k = int(sys.stdin.readline())
    for _ in range(k):
        cmd, n = sys.stdin.readline().split()
        n = int(n)
        if cmd == "I":
            heapq.heappush(min_q, n)
            heapq.heappush(max_q, (-n, n))
            if n in num:
                num[n] += 1
            else:
                num[n] = 1
        elif cmd == "D":
            if n < 0:
                while min_q and num[min_q[0]] == 0:
                    heapq.heappop(min_q)
                if not min_q:
                    continue
                i = heapq.heappop(min_q)
                num[i] -= 1
            else:
                while max_q and num[max_q[0][1]] == 0:
                    heapq.heappop(max_q)
                if not max_q:
                    continue
                i = heapq.heappop(max_q)[1]
                num[i] -= 1
        while min_q and num[min_q[0]] == 0:
            heapq.heappop(min_q)
        while max_q and num[max_q[0][1]] == 0:
            heapq.heappop(max_q)
    if min_q:
        print(heapq.heappop(max_q)[1], heapq.heappop(min_q))
    else:
        print("EMPTY")
