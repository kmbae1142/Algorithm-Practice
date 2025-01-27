vote = {"Lion":0, "Tiger":0}
for _ in range(9):
    n = input()
    vote[n] += 1
if vote["Lion"] > vote["Tiger"]:
    print("Lion")
else:
    print("Tiger")