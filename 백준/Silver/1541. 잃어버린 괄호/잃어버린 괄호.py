import sys
input = sys.stdin.readline

def calculate(s: str):
    parse = map(int, s.split('+'))
    return sum(parse)

s = input().strip().split('-')
ans = 0

if s[0] != '':
    if '+' in s[0]: ans += calculate(s[0])
    else: ans += int(s[0])

for i in range(1, len(s)):
    if '+' in s[i]: ans -= calculate(s[i])
    else: ans -= int(s[i])

print(ans)