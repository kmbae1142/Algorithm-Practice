prog = input()

if '_' in prog:
    cpp = prog.split('_')
    check = 0

    for i in cpp:
        if i.lower() != i or i == '':
            check = 1
            break

    if check:
        print("Error!")
    else:
        for i in range(1, len(cpp)):
            cpp[i] = cpp[i].capitalize()
        print(''.join(cpp))
else:
    java = list(prog)
    tocpp = []
    if java[0][0].isupper():
        print("Error!")
    else:
        temp = ""
        for i in java:
            if i.islower():
                temp += i
            else:
                tocpp.append(temp)
                temp = ""
                temp += i.lower()
        tocpp.append(temp)
        print('_'.join(tocpp))