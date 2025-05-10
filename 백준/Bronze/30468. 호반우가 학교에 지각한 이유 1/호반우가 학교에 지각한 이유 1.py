s, d, i, l, n = map(int, input().split())
print(n*4-(s+d+i+l) if n*4-(s+d+i+l) > 0 else 0)