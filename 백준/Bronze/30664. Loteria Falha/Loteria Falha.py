while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num % 42 == 0:
            print("PREMIADO")
        else:
            print("TENTE NOVAMENTE")