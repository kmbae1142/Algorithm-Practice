import sys
input = sys.stdin.readline

def mul_matrix(A, B, M):
    len_matrix = len(A)
    result = [[0] * len_matrix for _ in range(len_matrix)]
    for i in range(len_matrix):
        for l in range(len_matrix):
            for j in range(len_matrix):
                result[i][l] += (A[i][j] * B[j][l])
            result[i][l] %= M

    return result

while True:
    N, M, P = map(int, input().split())
    if N == 0 and M == 0 and P == 0:
        break
    A = [list(map(int, input().split())) for _ in range(N)]
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        result[i][i] = 1

    while P != 0:
        if P % 2:
            result = mul_matrix(result, A, M)
        A = mul_matrix(A, A, M)
        P //= 2

    for i in result:
        print(*i)
    print()