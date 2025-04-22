import sys
input = sys.stdin.readline

N = int(input())
h = list(map(int, input().split()))
print((sum(h) + 8 * (len(h) - 1)) // 24, (sum(h) + 8 * (len(h) - 1)) % 24)