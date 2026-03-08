while True:
    password = input()
    if password == "END":
        break
    for i in range(-1, -len(password) - 1, -1):
        print(password[i], end="")
    print()