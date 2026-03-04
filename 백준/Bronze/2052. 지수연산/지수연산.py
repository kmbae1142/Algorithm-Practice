N = int(input())
p = list(str(5 ** N))

ans = ["0", "."]
for _ in range(N - len(p)):
    ans.append("0")
ans += p
print("".join(ans))