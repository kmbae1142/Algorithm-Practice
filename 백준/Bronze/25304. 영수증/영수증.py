n = int(input())

sum = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    sum += a * b
    
if sum == n:
    print("Yes")
else:
    print("No")