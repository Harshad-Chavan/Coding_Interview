# Given an array of integers, return all triplets (a, b, c] such that a + b + c = 0. The
# solution must not contain duplicate triplets (e.g., [ 1, 2, 3] and [ 2, 3, 1] are Considered
# duplicate triplets), If no sud! triptets are found, return an empty array.
# Each triplet can be arranged in any order:, and the output can be returned in any order .
# Example:
# Input numbers = (0, -1, 2, -3, 1)
# Output [(-3, 1, 2], [-1, 0, ll]
from typing import List


def triplet_sum(arr: List[int]) -> List[int]:
    triplets = []
    arr.sort()
    for i in range(len(arr)):
        # we need target of zero hence if fisr element is greated than 0 break
        if arr[i] > 0:
            break
        # avoid duplicates phase 1
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        pairs = sorted_sum_all_pairs(arr, i + 1, -arr[i])
        for pair in pairs:
            triplets.append([arr[i]] + pair)
    return triplets


def sorted_sum_all_pairs(nums: List[int], start_point: int, target: int) -> List[int]:
    pairs = []
    if nums:
        left, right = start_point, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                pairs.append([nums[left], nums[right]])
                left = left + 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
        return pairs
    else:
        return pairs


if __name__ == "__main__":
    arr = [5, -1, -1, -2, 3]
    print(triplet_sum(arr))
