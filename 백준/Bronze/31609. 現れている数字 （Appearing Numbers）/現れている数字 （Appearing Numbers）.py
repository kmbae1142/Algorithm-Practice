n = int(input())
num = list(map(int, input().split()))
num = sorted(set(num))

for i in num:
    print(i)