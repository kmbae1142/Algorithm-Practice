def find(n, m, num: list):
    if len(num) == m:
        print(*num)
        return
    for i in range(1, n + 1):
        num.append(i)
        find(n, m, num)
        num.pop()

n, m = map(int, input().split())
num = []
find(n, m, num)