import sys
input = sys.stdin.readline

while True:
    sent = input().rstrip('\n')
    if sent == '***':
        break
    print(''.join(sent[::-1]))