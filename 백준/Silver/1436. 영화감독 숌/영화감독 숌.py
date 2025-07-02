ans = 0
n = int(input())

while True:
    if n == 0:
        break
    ans += 1
    if "666" in str(ans):
        n -= 1

print(ans)