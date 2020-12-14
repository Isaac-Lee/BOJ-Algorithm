from collections import deque


def topological_sort(graph, in_degree, nodes):
    answer = []
    stack = deque()
    for n in nodes:
        if in_degree[n] == 0:
            stack.append(n)
    while stack:
        node = stack.pop()
        answer.append(node)
        for n in graph[node]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                stack.append(n)
    return answer


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    in_degree = [0 for _ in range(n+1)]
    nodes = [i for i in range(1, n+1)]
    for _ in range(m):
        s1, s2 = map(int, input().split())
        graph[s1].append(s2)
        in_degree[s2] += 1
    print(*topological_sort(graph, in_degree, nodes))