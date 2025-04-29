A = input()
B = input()

A_and_B = []
A_or_B = []
A_xor_B = []
not_A = []
not_B = []

for i in range(100000):
    A_and_B.append(int(A[i]) & int(B[i]))
    A_or_B.append(int(A[i]) | int(B[i]))
    A_xor_B.append(int(A[i]) ^ int(B[i]))
    not_A.append(int(A[i]) ^ 1)
    not_B.append(int(B[i]) ^ 1)

print(''.join(map(str, A_and_B)))
print(''.join(map(str, A_or_B)))
print(''.join(map(str, A_xor_B)))
print(''.join(map(str, not_A)))
print(''.join(map(str, not_B)))