import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    card = list(input().strip().split())
    dq = deque([card[0]])
    for i in range(1, n):
        if ord(card[i]) <= ord(dq[0]):
            dq.appendleft(card[i])
        else:
            dq.append(card[i])
    print(''.join(dq))