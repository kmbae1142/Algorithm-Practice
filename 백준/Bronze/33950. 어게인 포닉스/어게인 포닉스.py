import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip().replace("PO", "PHO")
    print(s)