import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    X = int(input())
    form = ''.join(input().rstrip().split()).split('+')
    if '!' in form:
        print("!")
        continue
    form = list(map(int, form))
    if sum(form) > 9:
        print("!")
    else:
        print(sum(form))