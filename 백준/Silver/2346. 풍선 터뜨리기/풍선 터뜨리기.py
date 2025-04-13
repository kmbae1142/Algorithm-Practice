import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
order = deque((i + 1, int(v)) for i, v in enumerate(input().split()))
temp = order.popleft()
start = temp[1]
result = [temp[0]]

while len(order) > 0:
    if start > 0:
        for _ in range(start - 1):
            order.append(order.popleft())
    else:
        for _ in range(-start):
            order.appendleft(order.pop())
    temp = order.popleft()
    start = temp[1]
    result.append(temp[0])

print(*result)