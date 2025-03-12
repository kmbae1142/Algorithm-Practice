import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = input().strip()
    m = input().strip()
    h_d = 0

    for i, j in zip(n, m):
        if i != j:
            h_d += 1

    print(f"Hamming distance is {h_d}.")