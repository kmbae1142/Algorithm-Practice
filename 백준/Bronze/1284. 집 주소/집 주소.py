import sys
input = sys.stdin.readline

dic = {"1": 2, "0": 4}

while True:
    num = list(input().rstrip())
    if len(num) == 1 and num[0] == "0":
        break
    sum = 0
    for i in num:
        if i in dic.keys():
            sum += dic[i]
        else:
            sum += 3
    print(sum + len(num) + 1)