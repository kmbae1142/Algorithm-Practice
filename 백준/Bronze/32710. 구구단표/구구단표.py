n = int(input())
num = [0] * 101

for i in range(2, 10):
    for j in range(1, 10):
        num[i] = 1
        num[j] = 1
        num[i * j] = 1

if num[n]:
    print(1)
else:
    print(0)