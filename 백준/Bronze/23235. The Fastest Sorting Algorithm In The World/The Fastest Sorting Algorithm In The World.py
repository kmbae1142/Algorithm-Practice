import sys
i = 0
while True:
    arr = sys.stdin.readline().rstrip().split()
    if arr[0] == '0':
        break
    i += 1
    print(f"Case {i}: Sorting... done!")