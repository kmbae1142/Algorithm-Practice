import sys
num = int(input())
sum_ = 0
j = 0

str_ = sys.stdin.readline().rstrip()

for i in str_:
    sum_ += (ord(i) - 96) * 31**j
    j += 1

print(sum_ % 1234567891)