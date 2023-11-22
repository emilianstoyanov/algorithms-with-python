nums = [int(x) for x in input().split()]

flag_stop = True
counter = 0
for _ in range(len(nums) - counter):
    for idx in range(len(nums) - 1):

        first_idx = idx
        second_idx = idx + 1

        if nums[idx] > nums[idx + 1]:
            flag_stop = False
            nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]

    counter += 1
    if flag_stop:
        break
    else:
        flag_stop = True

print(*nums)
