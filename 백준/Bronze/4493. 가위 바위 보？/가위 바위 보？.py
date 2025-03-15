import sys
input = sys.stdin.readline

for _ in range(int(input())):
    rps = []
    p1 = 0
    p2 = 0
    for _ in range(int(input())):
        rps.append(input().strip().split())
    for i, j in rps:
        if i == j:
            continue
        if (i == 'R' and j == 'S') or (i == 'S' and j == 'P') or (i == 'P' and j == 'R'):
            p1 += 1
        else:
            p2 += 1
    if p1 == p2:
        print("TIE")
    elif p1 > p2:
        print("Player 1")
    else:
        print("Player 2")