import sys
input = sys.stdin.readline

while True:
    length = list(map(int, input().split()))
    length.sort()

    if length[0] == 0 and length[1] == 0 and length[2] == 0:
        break

    if length[0] + length[1] <= length[2]:
        print("Invalid")
    else:
        if length[0] == length[1] == length[2]:
            print("Equilateral")
        elif length[0] != length[1] != length[2]:
            print("Scalene")
        else:
            print("Isosceles")