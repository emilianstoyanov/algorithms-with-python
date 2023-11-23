# Insertion Sort

nums = [int(x) for x in input().split()]

for idx in range(len(nums)):

    while idx > 0 and nums[idx - 1] > nums[idx]:
        nums[idx - 1], nums[idx] = nums[idx], nums[idx - 1]
        idx -= 1

print(nums)
# 5 4 3 2 1
