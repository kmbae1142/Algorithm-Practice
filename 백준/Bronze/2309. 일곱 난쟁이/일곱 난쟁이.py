import sys
input = sys.stdin.readline

h = [int(input()) for _ in range(9)]
h_exist = [0] * 100
h.sort()
two = []
for i in h:
    h_exist[i] = 1

diff = sum(h) - 100
for height in h:
    if diff - height >= 0 and diff - height < 100:
        if h_exist[diff - height]:
            two.append(height)
            two.append(diff - height)
            break

for i in h:
    if i not in two:
        print(i)