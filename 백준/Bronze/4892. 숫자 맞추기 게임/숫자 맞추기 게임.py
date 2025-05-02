i = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = n0 * 3
    n4 = n0 // 2 if n1 % 2 == 0 else (n0 - 1) // 2
    if n1 % 2 == 0:
        print(f"{i}. even {n4}")
    else:
        print(f"{i}. odd {n4}")
    i += 1