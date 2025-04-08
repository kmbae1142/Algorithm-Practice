import sys
input = sys.stdin.readline

while True:
    str = input().rstrip()
    stack = []
    small = ['(', ')']
    big = ['[', ']']
    if str == '.':
        break

    for i in str:
        if i in ['(', ')', '[', ']']:
            stack.append(i)
        if stack[-2:] == small or stack[-2:] == big:
            del stack[-2:]

    print("yes" if not stack else "no")