S = input()
ans = "SciComLove"
count = 0

for i, j in zip(S, ans):
    if i != j:
        count += 1
print(count)