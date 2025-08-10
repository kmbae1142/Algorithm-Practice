import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

cnt = 0

def dfs(graph, V, visited, dist, order):
    global cnt
    visited[V] = True
    graph[V].sort(reverse=True)
    cnt += 1
    order[V] = cnt

    for i in graph[V]:
        if not visited[i]:
            dist[i] = dist[V] + 1
            dfs(graph, i, visited, dist, order)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
dist = [0] * (N + 1)
order = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, R, visited, dist, order)
print(sum([i * j for i, j in zip(order[1:], dist[1:])]))