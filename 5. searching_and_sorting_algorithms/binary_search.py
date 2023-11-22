def linear_search(nums, target):
    for idx, num in enumerate(nums):

        if num == target:
            return idx
    return -1


nums = [1, 2, 3, 4, 5]
target = 3

print(linear_search(nums, target))
