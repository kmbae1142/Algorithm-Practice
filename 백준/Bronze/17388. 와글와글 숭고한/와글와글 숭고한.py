dic = {"Soongsil":0, "Korea":0, "Hanyang":0}
S, K, H = map(int, input().split())
dic["Soongsil"] = S
dic["Korea"] = K
dic["Hanyang"] = H

if S + K + H >= 100:
    print("OK")
else:
    result = sorted(dic.items(), key=lambda x: x[1])
    print(result[0][0])