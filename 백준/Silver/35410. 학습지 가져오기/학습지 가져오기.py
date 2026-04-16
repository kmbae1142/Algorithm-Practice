import sys
input = sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))
t.sort()

min_time = 0
for i in t:
    min_time = max(min_time, i) + 1

print(min_time)