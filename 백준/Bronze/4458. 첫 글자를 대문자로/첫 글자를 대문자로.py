import sys
input = sys.stdin.readline

for _ in range(int(input())):
    str = list(input().rstrip())
    str[0] = str[0].upper()
    print(''.join(str))