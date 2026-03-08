import sys

for i in range(3):
    numbers = []
    num = int(input())

    for j in range(num):
        number = int(sys.stdin.readline().strip())
        numbers.append(number)

    if sum(numbers) > 0:
        print("+")
    elif sum(numbers) == 0:
        print("0")
    else:
        print("-")
        