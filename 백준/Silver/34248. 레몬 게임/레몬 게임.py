import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
s = [A[0]]

for i in A[1:]:
    if not s:
        s.append(i)
    elif s[-1] + i == 3:
        s.pop()
    elif sum(s) + i == 3:
        s.clear()
    else:
        s.append(i)

print("Yes" if not s else "No")