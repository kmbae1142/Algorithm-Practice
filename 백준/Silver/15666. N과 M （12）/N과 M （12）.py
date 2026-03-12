import sys
from collections import Counter
input = sys.stdin.readline

def find(N, M, num: list, ans: list):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        if not ans or (num[i] >= ans[-1]):
            ans.append(num[i])
            find(N, M, num, ans)
            ans.pop()

N, M = map(int, input().split())
num = list(map(int, input().split()))

list_set_num = sorted(list(set(num)))
find(len(list_set_num), M, list_set_num, [])