import sys
input = sys.stdin.readline

T = int(input())
for n in range(T):
    prog = []
    pointer = [0] * 32768
    current_ptr = 0
    stack = []
    result = []
    err = 0
    index = 0
    dic = dict()

    while True:
        temp = input().rstrip()
        if temp == "end":
            break
        parse_comment = temp.split('%')
        if len(parse_comment) >= 2:
            parse_comment.pop()
            prog.append(''.join(parse_comment))
        else:
            prog.append(temp)

    prog = list(''.join(prog))
    len_of_prog = len(prog)

    for i in range(len_of_prog):
        if prog[i] == '[':
            stack.append(i)
        elif prog[i] == ']':
            if not stack:
                err = 1
                break
            else:
                pair_index = stack.pop()
                dic[pair_index] = i
                dic[i] = pair_index

    if stack:
        err = 1

    if not err:
        while index < len_of_prog:
            com = prog[index]

            if com == '[':
                if pointer[current_ptr] == 0:
                    index = dic[index]
                    continue
            elif com == ']':
                if pointer[current_ptr] != 0:
                    index = dic[index]
                    continue
            elif com == '+':
                if pointer[current_ptr] == 255:
                    pointer[current_ptr] = 0
                else:
                    pointer[current_ptr] += 1
            elif com == '-':
                if pointer[current_ptr] == 0:
                    pointer[current_ptr] = 255
                else:
                    pointer[current_ptr] -= 1
            elif com == '>':
                if current_ptr == 32767:
                    current_ptr = 0
                else:
                    current_ptr += 1
            elif com == '<':
                if current_ptr == 0:
                    current_ptr = 32767
                else:
                    current_ptr -= 1
            elif com == '.':
                result.append(chr(pointer[current_ptr]))

            index += 1

        print(f"PROGRAM #{n + 1}:")
        print(''.join(result))
    else:
        print(f"PROGRAM #{n + 1}:")
        print("COMPILE ERROR")