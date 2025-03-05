x = int(input())
y = int(input())

print(f"All positions change in year {x}")
while x + 60 <= y:
    x += 60
    print(f"All positions change in year {x}")