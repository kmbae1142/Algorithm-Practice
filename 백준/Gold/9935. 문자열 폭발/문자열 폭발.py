s = input()
bomb_str = list(input())
len_bomb_str = len(bomb_str)
stack = []

for i in s:
    stack.append(i)
    if stack[-len_bomb_str:] == bomb_str:
        del stack[-len_bomb_str:]

print(''.join(stack) if len(stack) > 0 else "FRULA")