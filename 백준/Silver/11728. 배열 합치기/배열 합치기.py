import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B
C.sort()
print(*C)