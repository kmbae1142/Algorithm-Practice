import sys
input = sys.stdin.readline

plist = []
count = 0

for _ in range(5):
    count += 1
    p = list(input().rstrip())
    for i in range(len(p) - 2):
        if p[i] + p[i + 1] + p[i + 2] == 'FBI':
            plist.append(count)
            break

if len(plist):
    print(*plist)
else:
    print("HE GOT AWAY!")