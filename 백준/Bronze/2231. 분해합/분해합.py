N = int(input())

exist = 0
for i in range(1, N + 1):
    div = [i]
    temp = list(map(int, str(i)))
    div += temp
    if sum(div) == N:
        print(i)
        exist = 1
        break
if not exist:
    print(0)