import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, V, visited, dist):
    visited[V] = True
    graph[V].sort()
    for i in graph[V]:
        if not visited[i]:
            dist[i] = dist[V] + 1
            dfs(graph, i, visited, dist)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
dist = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, R, visited, dist)
for i, j in zip(visited[1:], dist[1:]):
    if i:
        print(j)
    else:
        print(-1)