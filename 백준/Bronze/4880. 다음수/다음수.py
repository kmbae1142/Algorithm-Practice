import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if b - a == c - b:
        print("AP " + str(c + b - a))
    else:
        print("GP " + str(c * (b // a)))