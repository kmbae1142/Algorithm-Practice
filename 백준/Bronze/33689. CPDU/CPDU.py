import sys
input = sys.stdin.readline

count = 0
for _ in range(int(input())):
    s = input().rstrip()
    if s[0] == 'C':
        count += 1
print(count)