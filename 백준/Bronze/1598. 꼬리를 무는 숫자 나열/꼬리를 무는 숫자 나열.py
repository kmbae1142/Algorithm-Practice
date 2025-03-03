def find(num):
    min, max = 1, 4
    while not (min <= num <= max):
        min += 4
        max += 4
    return max // 4

n, m = map(int, input().split())
row = []
col = []

row.append(n % 4 if n % 4 != 0 else 4)
row.append(m % 4 if m % 4 != 0 else 4)

col.append(find(n))
col.append(find(m))

print(abs(row[0] - row[1]) + abs(col[0] - col[1]))