def find(n):
    num = list(range(1, n + 1))
    left = 0
    right = 0
    sum_of_nums = 0
    cnt = 0

    while right < n:
        if sum_of_nums == n:
            cnt += 1
            sum_of_nums += num[right]
            right += 1
        elif sum_of_nums < n:
            sum_of_nums += num[right]
            right += 1
        else:
            sum_of_nums -= num[left]
            left += 1

    return cnt

print(find(int(input())) + 1)