s, d = map(int, input().split())

if s >= d and (s + d) % 2 == 0 and (s - d) % 2 == 0:
    t1 = (s + d) // 2
    t2 = (s - d) // 2
    print(t1, t2)
else:
    print(-1)