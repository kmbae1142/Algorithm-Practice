import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

order = 0

def dfs(graph, V, visited, visit_order):
    global order
    visited[V] = True
    order += 1
    visit_order[V] = order
    for i in sorted(graph[V]):
        if not visited[i]:
            dfs(graph, i, visited, visit_order)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
visit_order = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, R, visited, visit_order)
for i in visit_order[1:]:
    print(i)