from sys import stdin
input = stdin.readline

N, C = map(int, input().split())
message = list(map(int, input().split()))
dic = {}

for i in message:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
for i, j in result:
    for _ in range(j):
        print(i, end=' ')