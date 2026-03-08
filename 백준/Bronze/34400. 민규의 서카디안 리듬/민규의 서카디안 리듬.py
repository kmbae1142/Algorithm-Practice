import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = int(input())
    if t % 25 + 0.5 > 17:
        print("OFFLINE")
    else:
        print("ONLINE")