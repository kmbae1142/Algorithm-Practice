import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, V, visited, parent):
    visited[V] = True
    for i in graph[V]:
        if not visited[i]:
            parent[i] = V
            dfs(graph, i, visited, parent)

N = int(input())
graph = [[] for _ in range(N + 1)] # 0번은 사용하지 않음
visited = [False] * (N + 1)
parent = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited, parent)
for i in parent[2:]:
    print(i)