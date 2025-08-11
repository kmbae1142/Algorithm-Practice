import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, V):
    cnt = 1
    visited = [False] * len(graph)
    visited[V] = True
    queue = deque([V])
    depth = [0] * len(graph)
    order = [0] * len(graph)
    order[V] = cnt

    while queue:
        v = queue.popleft()
        graph[v].sort(reverse=True)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                depth[i] = depth[v] + 1
                cnt += 1
                order[i] = cnt

    return sum([k * l for k, l in zip(order[1:], depth[1:])])

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(graph, R))