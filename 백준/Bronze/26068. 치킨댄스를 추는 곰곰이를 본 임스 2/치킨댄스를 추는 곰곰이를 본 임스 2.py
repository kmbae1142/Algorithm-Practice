gift = 0
for _ in range(int(input())):
    dday = int(input().split("-")[1])
    if dday <= 90: gift += 1
print(gift)