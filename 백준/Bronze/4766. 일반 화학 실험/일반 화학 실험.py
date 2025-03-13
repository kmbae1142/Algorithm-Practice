deg = []
while True:
    n = float(input())
    if int(n) == 999:
        break
    deg.append(n)

for i in range(len(deg) - 1):
    print("%.2f" % (deg[i + 1] - deg[i]))