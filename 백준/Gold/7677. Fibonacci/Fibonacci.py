fibo = [0, 1]
p = 15 * 1000

for i in range(2, p):
    fibo.append((fibo[i - 2] + fibo[i - 1]) % 10000)

while True:
    n = int(input())
    if n == -1:
        break
    print(int(str(fibo[n % p])[-4:]))