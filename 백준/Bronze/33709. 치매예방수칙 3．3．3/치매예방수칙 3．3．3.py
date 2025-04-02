import re
n = int(input())
str = list(map(int, re.split(r'[.|:#]', input())))
print(sum(str))