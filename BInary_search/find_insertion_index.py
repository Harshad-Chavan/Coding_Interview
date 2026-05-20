# Given a sorted array of unique integers and a target integer, return the index of the
# target if it exists in the array. If the target is not present, return the index
# where it would be inserted to keep the array sorted.
#
# Example 1:
# Input:  nums = [1, 2, 4, 5, 7, 8, 9], target = 4
# Output: 2
#
# Example 2:
# Input:  nums = [1, 2, 4, 5, 7, 8, 9], target = 6
# Output: 4
# Explanation: 6 would be inserted at index 4 to be positioned between 5 and 7:
# [1, 2, 4, 5, 6, 7, 8, 9]
#
# Constraints:
# - nums is sorted in ascending order and contains unique values.
# - Return value is an integer index between 0 and len(nums).
# - Expected optimal time complexity: O(log n) using binary search.


def find_insertion_index(nums, target):

    l, r = 0, len(nums)
    while l < r:
        print(f"nums:{nums[l:r]}")  # exit
        mid = (r + l) // 2
        print(f"mid:{nums[mid]}")

        # its greater than equal to as mid can also be the target
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1

    return l


if __name__ == "__main__":
    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 4
    print(find_insertion_index(nums, target))
    target = 6
    print(find_insertion_index(nums, target))
