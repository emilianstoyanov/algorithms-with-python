

array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

reverser_list = []
for i in range(len(array) - 1, -1, -1):

    reverser_list.append(array[i])

print(reverser_list)

























# INSERT SORT ALGORITHM
# nums = [int(x) for x in input().split(' ')]
#
# for idx in range(0, len(nums)):
#     while idx > 0 and nums[idx] < nums[idx - 1]:
#         nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
#
#         idx -= 1
#
#
# print(*nums)

# def insert_algorithm(nums):
#     for idx in range(1, len(nums)):
#         for j in range(idx, 0, -1):
#
#             if nums[j] < nums[j - 1]:
#                 nums[j - 1], nums[j] = nums[j], nums[j - 1]
#             else:
#                 break
#     return nums
#
# nums = [int(x) for x in input().split(' ')]
# result = insert_algorithm(nums)
#
# print(*result)

# Binary search
# Only sorted arrays!!!

# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#
#     while left <= right:
#         mid_idx = (left + right) // 2
#         mid_number = numbers[mid_idx]
#         test = numbers[left:right]
#
#         if target == mid_number:
#             return mid_idx
#
#         if target > mid_number:
#             left = mid_idx + 1
#         else:
#             right = mid_idx - 1
#
#     return mid_idx
#
#
# numbers = [int(x) for x in input().split(' ')]
# target = int(input())
#
# result = binary_search(numbers, target)
# print(result)

# Linear search
# def linear_search(numbers, target):
#     for idx, num in enumerate(numbers):
#
#         if numbers[idx] == target:
#             return idx
#
#     return "Number does not exist"
#
#
# numbers = [int(x) for x in input().split(' ')]
#
# target = int(input())
#
# result = linear_search(numbers, target)
#
# print(result)

# def maxProfit(prices):
#     l = 0
#     max_profit = 0
#
#     for r in range(1, len(prices)):
#         profit = prices[r] - prices[l]
#
#         if profit > 0:
#             max_profit = max(profit, max_profit)
#
#         else:
#             l = r
#
#     return max_profit
#
#
# result = maxProfit([1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# print(result)
