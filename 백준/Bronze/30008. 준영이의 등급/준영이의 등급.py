n, k = map(int, input().split())
p = list(map(lambda x: int(x) * 100 // n, input().split()))

for i in p:
    if i > 96: print(9, end=' ')
    elif i > 89: print(8, end=' ')
    elif i > 77: print(7, end=' ')
    elif i > 60: print(6, end=' ')
    elif i > 40: print(5, end=' ')
    elif i > 23: print(4, end=' ')
    elif i > 11: print(3, end=' ')
    elif i > 4: print(2, end=' ')
    else: print(1, end=' ')