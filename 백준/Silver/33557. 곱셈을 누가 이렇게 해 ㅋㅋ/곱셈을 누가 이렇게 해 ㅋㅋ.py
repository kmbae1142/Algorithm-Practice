import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A = list(input().rstrip().split())
    real = str(int(A[0]) * int(A[1]))
    A[0], A[1] = list(A[0]), list(A[1])
    A[0].reverse(), A[1].reverse()
    len_long = len(A[0]) if len(A[0]) > len(A[1]) else len(A[1])
    bigger = A[0] if len(A[0]) > len(A[1]) else A[1]

    odd_mul = []

    for i in range(len_long):
        try:
            odd_mul.append(str(int(A[0][i]) * int(A[1][i])))
        except IndexError:
            odd_mul.append(str(bigger[i]))

    odd_mul.reverse()
    print(1 if real == ''.join(odd_mul) else 0)