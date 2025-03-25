N, B = input().split()
B = int(B)
str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = 1
sum = 0
N = N[::-1]

for i in N:
    sum += str.index(i) * n
    n *= B

print(sum)