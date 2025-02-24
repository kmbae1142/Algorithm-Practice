s = input()
stack = []
tag_index = []

for i in range(len(s)):
    if s[i] == "<":
        if len(tag_index) > 0:
            tag_index.reverse()
            print(''.join(tag_index), end='')
            tag_index.clear()
        stack.append(s[i])
        print(s[i], end='')
        continue

    if "<" in stack and not s[i] == ">":
        print(s[i], end='')
    elif s[i] == ">":
        print(s[i], end='')
        stack.clear()
    elif s[i] == " ":
        tag_index.reverse()
        print(''.join(tag_index), end=' ')
        tag_index.clear()
    else:
        tag_index.append(s[i])

tag_index.reverse()
print(''.join(tag_index))