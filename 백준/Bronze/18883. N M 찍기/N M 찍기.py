N, M = map(int, input().split())
i = 0

for _ in range(N):
    for j in range(M):
        i += 1
        if j == M - 1:
            print(i, end='')
        else:
            print(i, end=' ')
    print()