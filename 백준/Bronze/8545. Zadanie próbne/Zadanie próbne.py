str = input()
str1 = list(str)
str1.sort()
str1.sort(reverse = True)

for i in range(len(str1)):
    print(str1[i], end="")