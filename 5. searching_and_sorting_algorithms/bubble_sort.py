nums = [int(x) for x in input().split()]

is_sorted = False
counter = 0
while not is_sorted:
    is_sorted = True

    for idx in range(len(nums) - 1 - counter):
        if nums[idx] > nums[idx + 1]:
            nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
            is_sorted = False

    counter += 1

print(*nums)

# nums = [int(x) for x in input().split()]
#
# flag_stop = True
# counter = 0
# for _ in range(len(nums) - counter):
#     for idx in range(len(nums) - 1):
#
#         first_idx = idx
#         second_idx = idx + 1
#
#         if nums[idx] > nums[idx + 1]:
#             flag_stop = False
#             nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]
#
#     counter += 1
#     if flag_stop:
#         break
#     else:
#         flag_stop = True
#
# print(*nums)

# 24 9 80 41 66 1 54 31 55 33 88 35 32 4 20 19 76 48 98 36 76 49 83 21 44 12 85 68 18 12 27 28 29 21 22 37 74 78 34 15 71 75 33 54 20 40 60 56 51 51 25 77 75 46 47 57 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51 75 29 64 0 36
