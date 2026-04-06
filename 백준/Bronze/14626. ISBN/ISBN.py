isbn = list(input())
sum = 0
index = 0
for i in range(len(isbn)):
    if isbn[i] == '*':
        index = i + 1
        continue
    if i % 2:
        sum += int(isbn[i]) * 3
    else:
        sum += int(isbn[i])

if sum % 10 == 0:
    print(0)
elif index % 2:
    print(10 - sum % 10)
else:
    s = 10 - sum % 10 + sum
    while True:
        if (s - sum) % 3 == 0:
            print((s - sum) // 3)
            break
        else:
            s += 10