num = input()

if '7' not in num and int(num) % 7 != 0:
    print("0")
elif '7' not in num and int(num) % 7 == 0:
    print("1")
elif '7' in num and int(num) % 7 != 0:
    print("2")
elif '7' in num and int(num) % 7 == 0:
    print("3")