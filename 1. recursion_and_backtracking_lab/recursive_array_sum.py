def recursive_array_sum(numbers, idx):
    # base case
    if idx == len(numbers) - 1:
        return numbers[idx]
    # recursive call
    return numbers[idx] + recursive_array_sum(numbers, idx + 1)


# 1 2 3 4 5
nums = [int(x) for x in input().split()]
print(recursive_array_sum(nums, 0))
