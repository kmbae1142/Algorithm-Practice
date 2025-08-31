import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def test(preorder: list, graph: dict):
    if not preorder:
        return None
    root = preorder[0]
    graph[root] = []
    left_subtree = [i for i in preorder[1:] if i < root]
    right_subtree = [i for i in preorder[1:] if i > root]

    left = test(left_subtree, graph)
    if left is not None:
        graph[root].append(left)

    right = test(right_subtree, graph)
    if right is not None:
        graph[root].append(right)

    return root

def postorder(root, graph):
    try:
        postorder(graph[root][0], graph)
    except IndexError:
        pass
    try:
        postorder(graph[root][1], graph)
    except IndexError:
        pass
    print(root)

pre_traversal_result = []
graph = {}
while True:
    try:
        pre_traversal_result.append(int(input().strip()))
    except (EOFError, ValueError):
        break

test(pre_traversal_result, graph)
postorder(pre_traversal_result[0], graph)