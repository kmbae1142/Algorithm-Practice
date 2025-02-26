import sys
input = sys.stdin.readline

while True:
    b, n = map(int, input().split())
    if b == n == 0:
        break

    a = 0
    while True:
        a += 1
        if a ** n > b:
            break

    if a ** n == b:
        print(a)
    else:
        print(a - 1 if b - (a - 1) ** n < a ** n - b else a)