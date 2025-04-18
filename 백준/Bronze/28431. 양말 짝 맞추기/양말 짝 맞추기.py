socks = [int(input()) for _ in range(5)]
dic = {}
rem = 0

for i in socks:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

for i in dic.keys():
    if dic[i] % 2 != 0:
        rem = i

print(rem)