def check(list):
    for i in range(len(list) - 1, -1, -1):
        if int(list[i]) - int(list[i - 1]) < -1:
            return i
    return False

def find(n, num: list, prev):
    if n == 0:
        c = check(prev)
        if c > 1:
            del prev[c:len(prev)]
        else:
            prev.clear()
        return
    for i in range(n):
        if len(prev) == 0:
            temp = [str(n)]
        else:
            temp = prev
        temp.append(str(i))
        prev = temp
        num.append(int(''.join(temp)))
        find(i, num, prev)

n = int(input())
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
prev = []

for i in range(10):
    find(i, num, prev)

num.sort()

try:
    print(num[n])
except IndexError:
    print(-1)