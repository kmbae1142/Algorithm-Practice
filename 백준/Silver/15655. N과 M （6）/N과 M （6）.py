import sys
input = sys.stdin.readline

def find(N, M, num: list, ans: list):
    if len(ans) == M:
        print(*ans)
        return
    for i in num:
        if not ans or (i > ans[-1]):
            ans.append(i)
            find(N, M, num, ans)
            ans.pop()

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
find(N, M, num, [])