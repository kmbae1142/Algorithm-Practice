from collections import deque
N = int(input())
if N < 4:
    print("S" * N)
elif N == 4:
    print("SSHS")
else:
    dic = {0:'H', 1:'S', 2:'S'}
    dq = deque(list("SSHSS"))
    for i in range(6, N + 1):
        dq.appendleft(dic[i % 3])
    print(''.join(dq))