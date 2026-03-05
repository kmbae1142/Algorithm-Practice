import sys
import math
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N

for i in range(N):
    if A[i] - B > 0:
        ans += math.ceil((A[i] - B) / C)

print(ans)