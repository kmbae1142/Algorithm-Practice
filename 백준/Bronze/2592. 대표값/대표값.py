num = [int(input()) for i in range(10)]
dic = {}

for i in num:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(sum(num) // 10)
print(max(dic.items(), key=lambda x: x[1])[0])