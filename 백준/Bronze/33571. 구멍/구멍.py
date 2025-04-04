str = input()
hole = 0
hole1 = "AabDdegOoPpQqR@"
hole2 = "B"
for i in str:
    if i in hole1:
        hole += 1
    if i == hole2:
        hole += 2
print(hole)