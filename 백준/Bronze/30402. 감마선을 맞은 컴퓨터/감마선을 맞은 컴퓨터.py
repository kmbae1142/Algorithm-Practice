import sys
input = sys.stdin.readline

img = [list(input().rstrip().split()) for _ in range(15)]

for img in img:
    if 'w' in img:
        print("chunbae")
        break
    elif 'b' in img:
        print("nabi")
        break
    elif 'g' in img:
        print("yeongcheol")
        break