import sys
input = sys.stdin.read

html = input().strip().split()
a_cnt = 0
line = []

for word in html:
    if word == "<br>":
        if line:
            print(" ".join(line))
            line.clear()
            a_cnt = 0
        else:
            print()
            a_cnt = 0
    elif word == "<hr>":
        if line:
            print(" ".join(line))
            line.clear()
        print("-" * 80)
        a_cnt = 0
    elif a_cnt + len(word) > 80:
        print(" ".join(line))
        line.clear()
        line.append(word)
        a_cnt = len(word) + 1
    else:
        line.append(word)
        a_cnt += len(word) + 1

if line:
    print(" ".join(line))
