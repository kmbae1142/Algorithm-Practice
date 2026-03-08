num = int(input())
fact = 1

if num == 0:
    print("1")
else:
    for i in range(num):
        fact *= i + 1
    print(fact)