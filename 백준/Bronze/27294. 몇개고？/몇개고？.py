a, b = map(int, input().split())

if b == 1 or a < 12:
    print("280")
elif a >= 12 and a <= 16 and b == 0:
    print("320")
else:
    print("280")