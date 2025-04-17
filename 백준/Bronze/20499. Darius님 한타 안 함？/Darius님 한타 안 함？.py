kda = list(map(int, input().split('/')))
print("hasu" if kda[0] + kda[2] < kda[1] or kda[1] == 0 else "gosu")