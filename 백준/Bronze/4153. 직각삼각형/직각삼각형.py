while True:
    
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break;
        
    if (a > b and b > c) or (a > c and c > b):
        if b**2 + c**2 == a**2:
            print("right")
        else:
            print("wrong")
    elif (b > a and b > c) or (b > c and c > a):
        if a**2 + c**2 == b**2:
            print("right")
        else:
            print("wrong")
    else:
        if a**2 + b**2 == c**2:
            print("right")
        else:
            print("wrong")
