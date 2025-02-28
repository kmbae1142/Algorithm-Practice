from decimal import Decimal, getcontext

ab = input().split()
getcontext().prec = 2000
result = (Decimal(ab[0]) ** int(ab[1])).normalize()
print("{:f}".format(result))