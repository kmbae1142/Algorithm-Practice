db = {'a': 4, 'e': 3, 'i': 1, 'o': 0, 's': 5}
str = input()

for i in str:
    if i in db:
        print(db[i], end='')
    else:
        print(i, end='')