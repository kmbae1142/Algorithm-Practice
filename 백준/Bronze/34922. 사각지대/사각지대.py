import math

w, h = map(int, input().split())
r = int(input())

result = w * h - 0.25 * r * r * math.pi
print("%.2f" % result)