import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = [int(i) for i in input().split()]
score.sort(reverse=True)
print(score[k - 1])