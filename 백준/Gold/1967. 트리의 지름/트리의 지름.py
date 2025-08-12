import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, V, visited, dist):
    visited[V] = True
    for neighbor, weight in graph[V]:
        if not visited[neighbor]:
            dist[neighbor] = dist[V] + weight
            dfs(graph, neighbor, visited, dist)


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [0] * (n + 1)

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

dfs(graph, 1, visited, dist)
far = dist.index(max(dist))
dist = [0] * (n + 1)
visited = [False] * (n + 1)
dfs(graph, far, visited, dist)

print(max(dist))