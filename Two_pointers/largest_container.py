# You are given an array of numbers, each representing the height of a vertical line on a graph.
# A container can be formed with any pair of these lines, along with the x-axis of the graph.
# Return the amount of water which the largest container can hold.
#
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The vertical lines are at indices 1 and 8 with heights 8 and 7.
#              The width is 7 (8-1) and the minimum height is 7, so area = 7 * 7 = 49
#
# Diagram Example:
#              |
#          |   |               |
#          |   |       |       |
#      |   |   |   |   |   |   |   |   |
#      |___|___|___|___|___|___|___|___|
#      0   1   2   3   4   5   6   7   8
#    height=[1,8,6,2,5,4,8,3,7]
#
# The container between index 1 (height 8) and index 8 (height 7) holds the most water.
# Water held = min(height[1], height[8]) * (8 - 1) = min(8, 7) * 7 = 49
#
# Example 2:
# Input: height = [1,1]
# Output: 1
# Explanation: The two lines at indices 0 and 1 with heights 1 and 1.
#              The width is 1 (1-0) and the minimum height is 1, so area = 1 * 1 = 1
from typing import List


def largest_container(nums: List[int]) -> int:
    max_water = 0
    left, right = 0, len(nums) - 1
    while left < right:
        water = min(nums[left], nums[right]) * (right - left)
        if water > max_water:
            max_water = water
        if nums[left] < nums[right]:
            left += 1
        elif nums[left] > nums[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water


if __name__ == "__main__":
    heights = [2, 7, 8, 3, 7, 6]

    print(largest_container(heights))
