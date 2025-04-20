import sys
input = sys.stdin.readline

max = -1

for _ in range(int(input())):
    h, w = map(int, input().split())
    if max < h * w:
        max = h * w

print(max)