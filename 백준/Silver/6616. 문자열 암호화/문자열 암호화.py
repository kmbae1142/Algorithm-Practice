import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    str = list(input().rstrip().split())
    new_str = "".join(str).upper()
    strlen = len(new_str)
    encrypted = [""] * strlen
    index = 0
    startPos = 0

    for i in range(strlen):
        if index > strlen - 1:
            startPos += 1
            index = startPos
        encrypted[index] = new_str[i]
        index += n

    # index에 n씩 더하면서 암호화를 시켜준다. 이때 문자열의 끝에 도달했는지를 알기 위해
    # 조건 검사를 해준다. 

    print("".join(encrypted))