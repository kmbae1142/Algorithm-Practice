import sys

num = int(input())
str = sys.stdin.readline().rstrip()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in str:
    if i in vowels:
        count += 1
    
print(count)