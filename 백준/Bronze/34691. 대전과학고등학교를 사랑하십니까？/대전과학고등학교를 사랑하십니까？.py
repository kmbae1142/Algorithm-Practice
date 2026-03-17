import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == "animal":
        print("Panthera tigris")
    elif s == "tree":
        print("Pinus densiflora")
    elif s == "flower":
        print("Forsythia koreana")
    else:
        break