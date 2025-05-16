import sys
input = sys.stdin.readline

N, K = map(int, input().split())
deg = list(map(int, input().split()))

s = sum(deg[:K])
li = [s]

for i in range(K, N):
    s += deg[i] - deg[i - K]
    li.append(s)

print(max(li))