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

for _ in range(n):
    info = list(map(int, input().split()))
    info.pop()
    p = info[0]
    child = [(info[i], info[i + 1]) for i in range(1, len(info), 2)]
    graph[p] = child

dfs(graph, 1, visited, dist)
far = dist.index(max(dist))
dist = [0] * (n + 1)
visited = [False] * (n + 1)
dfs(graph, far, visited, dist)

print(max(dist))