num = int(input())

V = num // 5
I = num % 5

for i in range(V):
    print("V", end='')
for i in range(I):
    print("I", end='')