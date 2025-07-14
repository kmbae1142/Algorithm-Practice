import sys
input = sys.stdin.readline

cnt = 0

def dfs(tree, V, visited, del_node):
    global cnt
    if V == del_node:
        return

    visited[V] = True
    if len(tree[V]) == 1 and (del_node in tree[V]):
        cnt += 1
    if len(tree[V]) == 0:
        cnt += 1

    for i in tree[V]:
        if not visited[i]:
            dfs(tree, i, visited, del_node)

N = int(input())
tree = [[] for _ in range(N)]
parent = list(map(int, input().split()))
root = parent.index(-1)
del_node = int(input())
visited = [False] * N

for i in range(N):
    if parent[i] != -1:
        #tree[i].append(parent[i])
        tree[parent[i]].append(i)

dfs(tree, root, visited, del_node)
print(cnt)