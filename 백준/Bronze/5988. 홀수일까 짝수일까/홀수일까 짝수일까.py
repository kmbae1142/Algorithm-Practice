import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = input().strip()
    if int(n[-1]) % 2 == 0:
        print("even")
    else:
        print("odd")