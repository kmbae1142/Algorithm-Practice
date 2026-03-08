num = int(input())
score_list = [float(i) for i in input().split()]

score_list.sort()
M = score_list[-1]

for i in range(num):
    score_list[i] = score_list[i] / M * 100

print(sum(score_list) / num)