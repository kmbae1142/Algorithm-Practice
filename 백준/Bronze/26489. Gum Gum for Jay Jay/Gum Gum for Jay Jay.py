count = 0

while True:
    try:
        str = input()
        if str == "gum gum for jay jay":
            count += 1
    except:
        break

print(count)