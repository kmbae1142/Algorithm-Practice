length = list(map(int, input().split()))
length.sort()

if length[0] == length[1] == length[2]:
    print(length[0] * 3)
elif length[0] + length[1] > length[2]:
    print(length[0] + length[1] + length[2])
else:
    print(2 * (length[0] + length[1]) - 1)