# Given an array of integers sorted in non-decreasing order, return the first and last indexes
# of a target number. If the target is not found, return [-1, -1].
#
# Example 1:
# Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
# Explanation: The first and last occurrences of number 8 are at indexes 3 and 4, respectively.
#
# Example 2:
# Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]
# Explanation: Target 6 is not found in the array.
#
# Constraints:
# - nums is sorted in non-decreasing order.
# - Expected optimal time complexity: O(log n) using binary search.


def find_lower_bound(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (r + l) // 2
        print(nums[l : r + 1])

        # if the target is less than mid that means lower bound is before mid
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    return l if nums and nums[l] == target else -1


def find_upper_bound(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = ((r + l) // 2) + 1
        print(nums[l : r + 1])

        # if the target is less than mid that means upper bound is before mid
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            l = mid

    return r if nums and nums[r] == target else -1


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 8, 10]
    target = 8

    lower_bound = find_lower_bound(nums, target)
    upper_bound = find_upper_bound(nums, target)

    print(lower_bound, upper_bound)
