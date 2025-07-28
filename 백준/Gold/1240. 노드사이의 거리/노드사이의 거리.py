import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, V, target):
    visited = [False] * len(graph)
    queue = deque([V])
    visited[V] = True
    dist = [0] * len(graph)

    while queue:
        v = queue.popleft()
        for neighbor, weight in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[v] + weight
                if neighbor == target:
                    return dist[neighbor]
                queue.append(neighbor)
    return

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

for _ in range(M):
    start, end = map(int, input().split())
    print(bfs(graph, start, end))