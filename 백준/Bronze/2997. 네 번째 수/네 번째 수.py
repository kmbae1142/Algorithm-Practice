num = list(map(int, input().split()))
num.sort()

if num[1] - num[0] == num[2] - num[1]:
    print(num[2] + num[2] - num[1])
else:
    if num[1] - num[0] < num[2] - num[1]:
        print((num[1] + num[2]) // 2)
    else:
        print((num[0] + num[1]) // 2)