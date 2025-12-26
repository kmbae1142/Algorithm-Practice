def mul_matrix(A, B):
    len_matrix = len(A)
    result = [[0] * len_matrix for _ in range(len_matrix)]
    for i in range(len_matrix):
        for l in range(len_matrix):
            for j in range(len_matrix):
                result[i][l] += (A[i][j] * B[j][l])
            result[i][l] %= 1000

    return result

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]
for i in range(N):
    result[i][i] = 1

while B != 0:
    if B % 2:
        result = mul_matrix(result, A)
    A = mul_matrix(A, A)
    B //= 2

for i in result:
    print(*i)