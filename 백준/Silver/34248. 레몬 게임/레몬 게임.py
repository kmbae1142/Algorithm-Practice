import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
s = [A[0]]

for i in A[1:]:
    if s and s[-1] + i == 3:
        s.pop()
    else:
        s.append(i)

if sum(s) == 3: s.clear()
print("Yes" if not s else "No")