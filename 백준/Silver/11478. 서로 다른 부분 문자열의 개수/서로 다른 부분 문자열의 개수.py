S = input()
substr = []

for i in range(len(S)):
    for j in range(i, len(S)):
        substr.append(S[i:j+1])

print(len(set(substr)))