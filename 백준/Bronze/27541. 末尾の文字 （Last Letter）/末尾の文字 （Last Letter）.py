n = int(input())
s = list(input())

if s[-1] == 'G':
    del s[-1]
    print(''.join(s))
else:
    s.append('G')
    print(''.join(s))