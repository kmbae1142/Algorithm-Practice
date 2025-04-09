import sys
input = sys.stdin.readline

n = int(input())
postfix = list(input().strip())
nums = []
stack = []
result = 0

for i in range(n):
    nums.append(int(input()))

for i in range(len(postfix)):
    if postfix[i].isalpha():
        postfix[i] = nums[ord(postfix[i]) - 65]

for i in postfix:
    if i == '*':
        result = stack[-2] * stack[-1]
        del stack[-2:]
        stack.append(result)
    elif i == '/':
        result = stack[-2] / stack[-1]
        del stack[-2:]
        stack.append(result)
    elif i == '+':
        result = stack[-2] + stack[-1]
        del stack[-2:]
        stack.append(result)
    elif i == '-':
        result = stack[-2] - stack[-1]
        del stack[-2:]
        stack.append(result)
    else:
        stack.append(i)

print(f"{stack[0]:.2f}")