n = int(input())
fibo = [0, 1] 
p = 15 * 100000

for i in range(2, p):
    fibo.append((fibo[i - 2] + fibo[i - 1]) % 1000000)

print(fibo[n % p])
