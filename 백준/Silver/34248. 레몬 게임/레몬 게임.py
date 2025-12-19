import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = []

stack.append(A[0])
for i in range(1, N):
    if stack and stack[-1] + A[i] == 3:
        stack.pop()
    elif sum(stack) + A[i] == 3:
        stack.clear()
    else:
        stack.append(A[i])

if sum(stack) == 3: stack.clear()
print("Yes" if len(stack) == 0 else "No")