import sys
input = sys.stdin.readline

def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

n = int(input())
pos = [int(input()) for _ in range(n)]
diff = []
ans = 0

for i in range(1, len(pos)):
    diff.append(pos[i] - pos[i - 1])

gcd = diff[0]
for i in range(1, len(diff)):
    gcd = GCD(gcd, diff[i])

for i in diff:
    ans += i // gcd - 1

print(ans)