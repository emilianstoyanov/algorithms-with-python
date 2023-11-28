def sorted_squares(nums):
    left, right = 0, len(nums) - 1
    result = []

    while left <= right:

        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    return result[::-1]


# result = sorted_squares([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
result = sorted_squares([-3, -1, 0, 4])  # [0, 1, 9, 16]

print(result)
