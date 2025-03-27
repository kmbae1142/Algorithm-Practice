import sys
input = sys.stdin.readline

for _ in range(int(input())):
    c = int(input())
    q, d, n, p = 0, 0, 0, 0
    if c // 25 >= 1:
        q += c // 25
        c = c % 25
    if c // 10 >= 1:
        d += c // 10
        c = c % 10
    if c // 5 >= 1:
        n += c // 5
        c = c % 5
    p += c // 1
    print(q, d, n, p)