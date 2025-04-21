B = int(input())
P = 5 * B - 400

if P == 100:
    print(P, 0, sep='\n')
elif P < 100:
    print(P, 1, sep='\n')
else:
    print(P, -1, sep='\n')