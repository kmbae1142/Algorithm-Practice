import sys
input = sys.stdin.readline

perfect = ['(', ')']
for _ in range(int(input())):
    str = input().strip()
    stack = []
    for i in str:
        stack.append(i)
        if stack[-2:] == perfect:
            del stack[-2:]
    print("YES" if not stack else "NO")