import sys
input = sys.stdin.readline
from statistics import multimode

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

print(round(sum(nums) / len(nums)))
print(nums[len(nums) // 2])
li = sorted(multimode(nums))
print(li[0] if len(li) == 1 else li[1])
print(max(nums) - min(nums))