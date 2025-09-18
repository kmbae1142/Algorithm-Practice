import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    str = input().rstrip('\n')
    left, right = deque([]), deque([])

    for i in str:
        if i == '<':
            if left:
                right.appendleft(left.pop())
        elif i == '>':
            if right:
                left.append(right.popleft())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    print(''.join(left) + ''.join(right))