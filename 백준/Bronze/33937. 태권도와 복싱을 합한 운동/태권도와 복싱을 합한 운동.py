A = input()
B = input()
vowels = ['a', 'e', 'i', 'o', 'u']
index_A, index_B = 0, 0

for i in range(len(A) - 1):
    if A[i] in vowels:
        if A[i + 1] not in vowels:
            index_A = i + 1
            break
        elif A[i + 1] in vowels:
            continue
        else:
            break

for i in range(len(B) - 1):
    if B[i] in vowels:
        if B[i + 1] not in vowels:
            index_B = i + 1
            break
        elif B[i + 1] in vowels:
            continue
        else:
            break

if index_A == 0 or index_B == 0:
    print("no such exercise")
else:
    print(A[:index_A] + B[:index_B])