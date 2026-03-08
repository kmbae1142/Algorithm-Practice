arr = [int(i) for i in input().split()]
count = 0
for i in arr:
    if i == 9:
        count += 1

if count >= 1:
    print("F")
else:
    print("S")