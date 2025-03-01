import sys
input = sys.stdin.readline

for _ in range(int(input())):
    str = list(bin(int(input()))[2:])
    str.reverse()
    index = []
    for i in range(len(str)):
        if str[i] == '1':
            index.append(i)
    print(*index)