import re

N = int(input())
str = input()
paul_confirm = re.findall(r'[PAUL]+', str)
if ''.join(paul_confirm) == "PAUL":
    result = re.findall(r'[^PAUL]+', str)
    err = 0
    for i in result:
        if len(i) % 2 != 0:
            print("NO")
            err = 1
            break
    if not err: print("YES")
else:
    print("NO")