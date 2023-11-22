nums = [int(x) for x in input().split()]

for idx in range(len(nums)):
    min_idx = idx
    for curr_idx in range(idx + 1, len(nums)):
        if nums[curr_idx] < nums[min_idx]:
            min_idx = curr_idx
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

print(*nums)

# nums = [int(x) for x in input().split()]
#
# for old_value_idx in range(len(nums)):
#     current_number = nums[old_value_idx]
#     num_with_better_value_idx = old_value_idx
#
#     for next_idx in range(old_value_idx + 1, len(nums)):
#         next_number = nums[next_idx]
#
#         if next_number < current_number:
#             current_number = next_number
#             num_with_better_value_idx = next_idx
#
#     nums[old_value_idx], nums[num_with_better_value_idx] = nums[num_with_better_value_idx], nums[old_value_idx]
#
# print(*nums)
