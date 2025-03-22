def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


m = int(input())
n = int(input())
sum = 0
min = 10001

for i in range(m, n + 1):
    if isPrime(i):
        sum += i
        if min > i:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum, min, sep="\n")