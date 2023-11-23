nums = [int(x) for x in input().split()]

for i in range(len(nums)):
    idx = i
    while idx > 0 and nums[idx] < nums[idx - 1]:
        nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
        idx -= 1

print(*nums)
