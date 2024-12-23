import sys
input = sys.stdin.readline

R, C = map(int, input().split())
row_list = []
col_str = []
count = 0

for i in range(R):
    row = row_list.append(list(input().rstrip()))

for i in range(C):
    temp = []
    for j in range(R):
        temp.append(row_list[j][i])
    col_str.append(temp)

while True:
    for i in range(C):
        del col_str[i][0]
    test = list(set([tuple(col_str) for col_str in col_str]))
    if len(test) == len(col_str):
        count += 1
    else:
        break

print(count)