import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(graph, V, visited, order_list):
    order = 1
    visited[V] = True
    queue = deque([V])
    order_list[V] = order

    while queue:
        v = queue.popleft()
        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                order += 1
                order_list[i] = order

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
order_list = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(graph, R, visited, order_list)
print('\n'.join(map(str, order_list[1:])))