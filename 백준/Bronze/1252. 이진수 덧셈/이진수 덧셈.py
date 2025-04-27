a, b = input().split()
if len(a) > len(b): b = '0' * (len(a) - len(b)) + b
else: a = '0' * (len(b) - len(a)) + a
result = [0] * len(a)
a = list(map(int, a))
b = list(map(int, b))

carry = 0
for i in range(len(a) - 1, -1, -1):
    result[i] = a[i] ^ b[i] ^ carry
    carry = (a[i]&b[i]) | (b[i]&carry) | (a[i]&carry)

index = 0
if carry: result = [1] + result
if set(result) == {0}: 
    print(0)
else:
    for i in range(len(result)):
        if result[i] != 0:
            index = i
            break
    print(''.join(map(str, result[index:])))