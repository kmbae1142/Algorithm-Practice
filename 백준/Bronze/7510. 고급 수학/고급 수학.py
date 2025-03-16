import sys
input = sys.stdin.readline

for i in range(int(input())):
    li = list(map(int, input().split()))
    li.sort()
    print(f"Scenario #{i + 1}:")
    if li[2] ** 2 == li[1] ** 2 + li[0] ** 2:
        print("yes")
    else:
        print("no")
    print()