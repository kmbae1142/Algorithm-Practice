n, m = map(int, input().split())
nr = n % 4 if n % 4 != 0 else 4
mr = m % 4 if m % 4 != 0 else 4
nc = n // 4 if n % 4 != 0 else n // 4 - 1
mc = m // 4 if m % 4 != 0 else m // 4 - 1
print(abs(nr - mr) + abs(nc - mc))