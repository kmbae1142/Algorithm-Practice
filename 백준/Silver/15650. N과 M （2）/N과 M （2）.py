from itertools import combinations

n, m = map(int, input().split())
c = combinations(range(1, n + 1), m)
c = list(c)

for i in c:
    print(*i)