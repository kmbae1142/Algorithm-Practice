def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a


n1, n2 = map(int, input().split())
n3, n4 = map(int, input().split())

re1 = n4*n1 + n2*n3
re2 = n2*n4

print((n4*n1 + n2*n3) // Euclidean(re1, re2), n2*n4 // Euclidean(re1, re2))