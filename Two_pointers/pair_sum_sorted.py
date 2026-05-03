# Given an array of integers sorted in ascending order aAd a target value, return the index~s
# of any pair of numbers in the array that sum to the tar-get. The order of the indexes In the
# result doesn't matter. If no pair is found, return an empty array.
#
# Example 1:
# Input numbers ( -5, -2, 3, 4, 6]., target = 7
# Output (2, 3)
# Explanation: nums[2] + nums[3] = 3 + 4 = 7
from typing import List, Tuple

# Example 2:
# Input nums = [1, 1, 1], target = 2
# Output: (0, 1)
# Explanation: other valid outputs could be [ 1, 0] • [ e., 2] , [ 2, 0] , [ 1, 2] or [ 2,1]


# brute force
def pair_sum(arr: List[int], target: int) -> Tuple[List[int], List[int]]:
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return ([i, j], [arr[i], arr[j]])
    else:
        return []


def two_pointers(arr: List[int], target: int) -> List[int]:
    if arr:
        left, right = 0, len(arr) - 1
        while left < right:
            sum = arr[left] + arr[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left, right]
        return []
    else:
        return []


if __name__ == "__main__":
    print(pair_sum([-5, -2, 3, 4, 6], 7))
    print(two_pointers([-2, -3, -2], -4))
