import sys
from collections import Counter
input = sys.stdin.readline

def find(N, M, num: list, ans: list):
    global c
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        if c[num[i]] > 0:
            ans.append(num[i])
            c[num[i]] -= 1
            find(N, M, num, ans)
            c[num[i]] += 1
            ans.pop()

N, M = map(int, input().split())
num = list(map(int, input().split()))
c = Counter(num)

list_set_num = sorted(list(set(num)))
find(len(list_set_num), M, list_set_num, [])