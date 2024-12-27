from itertools import permutations

n, m = map(int, input().split())
p = permutations(range(1, n + 1), m)
p = list(p)

for i in p:
    print(*i)