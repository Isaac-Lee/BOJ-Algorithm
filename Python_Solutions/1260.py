def dfs(graph, start):
    visit = list()
    stack = list()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(sorted(graph[node], key=lambda x: -x))
    return visit


def bfs(graph, start):
    visit = list()
    queue = list()
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            graph[node].sort()
            queue.extend(graph[node])
    return visit


if __name__ == '__main__':
    debug = True
    n, m, s = map(int, input().split())
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for _ in range(m):
        k, v = map(int, input().split())
        # 양방향 간선의 경우 각각의 노드에 추가
        # 단방향의 경우 방향을 노려해서 하나만 노드에 추가
        graph[k].append(v)
        graph[v].append(k)
    print(*dfs(graph, s))
    print(*bfs(graph, s))