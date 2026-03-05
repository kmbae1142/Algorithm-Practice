A, B = map(int, input().split())
primes = [False, False] + [True] * (B - 1)
ans = 0

for i in range(2, int(B ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, B + 1, i):
            primes[j] = False

pnum = [i for i in range(2, B) if primes[i]]

for i in range(A, B + 1):
    if primes[i]:
        continue
    else:
        n = i
        pi = 0
        pf = 0
        while n != 1:
            if n % pnum[pi] == 0:
                pf += 1
                n //= pnum[pi]
            else:
                pi += 1
        if primes[pf]:
            ans += 1

print(ans)