# A palindrome is a sequence of characters that reads the same forward and backward.
# Given a string, determine if it's a palindrome after removing all non-alphanumeric characters.
# A character is alphanumeric if it's either a letter or a number.
# Example 1:
# Input: "race a car"
# Output: False
# Example 2:
# Input: "A man, a plan, a canal: Panama"
# Output: True
# Constraints:
# The string may include a combination of lowercase English letters, numbers, spaces, and
# punctuations.


def is_palindrome(nums: str) -> bool:
    left, right = 0, len(nums) - 1
    while left < right:
        while left < right and not nums[left].isalnum():
            left += 1
        while left < right and not nums[right].isalnum():
            right -= 1
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("racecar"))
    print(is_palindrome("abba"))
    print(is_palindrome("a!#bba"))
    print(is_palindrome("abc"))
