import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = input().strip()
    s = str(int(n) + int(n[::-1]))
    if s == s[::-1]: print("YES")
    else: print("NO")