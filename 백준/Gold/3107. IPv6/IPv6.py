IPv6 = list(input().split(":"))

for i in range(len(IPv6)):
    length = len(IPv6[i])

    if IPv6[i] == '' and (i == 0 or i == len(IPv6) - 1):
        continue

    if IPv6[i] == '' and i != 0:
        if IPv6[0] == '' or IPv6[-1] == '':
            lenOfIPv6 = len(IPv6) - 1
        else:
            lenOfIPv6 = len(IPv6)
        for j in range(8 - (lenOfIPv6 - 1)):
            print("0000", end='')
            if IPv6[-1] == '':
                if j != 7 - (lenOfIPv6 - 1):
                    print(":", end='')
            else:
                if j != 8 - (lenOfIPv6 - 1):
                    print(":", end='')
        continue

    if length < 4:
        if length != 0:
            IPv6[i] = '0' * (4 - length) + IPv6[i]
            print(IPv6[i], end='')
    else:
        print(IPv6[i], end='')

    if i != len(IPv6) - 1:
        print(":", end='')