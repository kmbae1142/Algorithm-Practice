n = int(input())
check = 1

while n < 9999:
    n += 1
    temp = str(n)
    if (int(temp[:2]) + int(temp[2:])) ** 2 == n:
        print(n)
        check = 0
        break


if check:
    print(-1)