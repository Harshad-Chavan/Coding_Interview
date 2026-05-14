# Given an array of integers, return the indexes of any two numbers that add up to a target.
# The order of the indexes in the result doesn't matter. If no pair is found, return an empty
# array.
#
# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9
#
# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Explanation: nums[1] + nums[2] = 2 + 4 = 6
#
# Example 3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 3 + 3 = 6
#
# Example 4:
# Input: nums = [1, 2, 3], target = 7
# Output: []
# Explanation: No pair found that adds up to 7
#
# Constraints:
# - You may not use the same element twice
# - You can assume that each input has exactly one solution (or none)

from typing import List


def pair_sum_unsorted(arr: List[int], target: int) -> List[int]:
    has_map = {}
    for i, value in enumerate(arr):
        comp = target - value
        if comp in has_map:
            return [has_map[comp], i]
        has_map[value] = i
    return []


if __name__ == "__main__":
    target = 9
    print(pair_sum_unsorted([2, 11, 5, 3, 15, 4], 5))
