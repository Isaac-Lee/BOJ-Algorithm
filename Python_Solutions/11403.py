from collections import deque
import sys

def BFS(start, end, graph):
    visit = set()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if (node, i) in visit:
                continue
            visit.add((node, i))
            if i == end:
                return True
            queue.append(i)
    return False

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    graph = {}
    answer = [[] for _ in range(n)]

    for i in range(n):
        graph[i] = []
        for j, v in enumerate(map(int, sys.stdin.readline().split())):
            if v == 1:
                graph[i].append(j)

    for i in range(n):
        for j in range(n):
            if BFS(i, j, graph):
                answer[i].append(1)
            else:
                answer[i].append(0)

    for line in answer:
        print(*line)
