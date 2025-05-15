expr = input()
precedence = {'+': 2, '-': 2, '*': 1, '/': 1}
oper_stack = []
result = []

for ch in expr:
    if ch == '(':
        oper_stack.append(ch)
    elif ch == ')':
        while oper_stack and oper_stack[-1] != '(':
            result.append(oper_stack.pop())
        oper_stack.pop()
    elif ch in precedence:
        while (oper_stack and oper_stack[-1] != '(' and
               precedence[oper_stack[-1]] <= precedence[ch]):
            result.append(oper_stack.pop())
        oper_stack.append(ch)
    else:
        result.append(ch)

while oper_stack:
    result.append(oper_stack.pop())

print(''.join(result))