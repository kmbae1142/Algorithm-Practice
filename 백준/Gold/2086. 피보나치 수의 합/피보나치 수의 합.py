mod = 1000000000

def matrix_mul(A, B):
    mul = [[0, 0], [0, 0]]

    mul[0][0] = (A[0][0] * B[0][0]) % mod + (A[0][1] * B[1][0]) % mod
    mul[0][1] = (A[0][0] * B[0][1]) % mod + (A[0][1] * B[1][1]) % mod
    mul[1][0] = (A[1][0] * B[0][0]) % mod + (A[1][1] * B[1][0]) % mod
    mul[1][1] = (A[1][0] * B[0][1]) % mod + (A[1][1] * B[1][1]) % mod

    return mul

def matrix_power(A, n):
    if n > 1:
        A = matrix_power(A, n // 2)
        A = matrix_mul(A, A)

        if n % 2 == 1:
            B = [[1, 1], [1, 0]]
            A = matrix_mul(A, B)

    return A

def fibo(n):
    A = [[1, 1], [1, 0]]
    A = matrix_power(A, n)
    return A[0][0]

a, b = map(int, input().split())
print((fibo(b + 1) - fibo(a)) % mod if a != b else fibo(a - 1) % mod)