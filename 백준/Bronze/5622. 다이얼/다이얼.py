phone_str = input()
num_to_str = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
str_to_num = []

for i in phone_str:
    for j in range(len(num_to_str)):
        if i in num_to_str[j]:
            str_to_num.append(j + 2)
            break

print(sum(str_to_num) + len(str_to_num))