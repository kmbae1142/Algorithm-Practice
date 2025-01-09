one = list(map(int, input().split()))
two = list(map(int, input().split()))

total_1 = 1 * one[0] + 2 * one[1] + 3 * one[2]
total_2 = 1 * two[0] + 2 * two[1] + 3 * two[2]

if total_1 > total_2:
    print(1)
elif total_1 < total_2:
    print(2)
else:
    print(0)