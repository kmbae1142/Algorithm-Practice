p = input()
parsing = []
temp = []
op = ['+', '-']

for i in p:
    if i in op:
        if temp:
            parsing.append(''.join(temp))
        parsing.append(i)
        temp = []
    else:
        temp.append(i)
parsing.append(''.join(temp))

for i in range(len(parsing)):
    if 'x' in parsing[i]:
        result = int(''.join(parsing[i][:len(parsing[i]) - 1])) // 2
        if result == 1:
            parsing[i] = 'xx'
        else:
            parsing[i] = str(result) + "xx"
    elif parsing[i] in op:
        continue
    else:
        if parsing[i] == '1':
            parsing[i] = 'x'
        elif parsing[i] == '0':
            parsing[i] = 'W'
        else:
            parsing[i] += 'x'

if 'W' not in parsing:
    parsing.append("+W")
print(''.join(parsing))