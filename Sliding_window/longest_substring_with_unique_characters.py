def longest_substrings(s):
    substrings = []
    l = r = 0
    hash_set = set()
    max_len = 0
    while r < len(s):

        # If we encounter a duplicate character in the window, shrink
        # the window until it's no longer a duplicate
        while s[r] in hash_set:
            hash_set.remove(s[l])
            l += 1
        max_len = max(max_len, r - l + 1)
        hash_set.add(s[r])
        r += 1

    return max_len


def longest_substring_optimized(s):
    l = r = 0
    hash_map = {}
    max_len = 0
    while r < len(s):

        if s[r] in hash_map and not hash_map[s[r]] < l:
            l = hash_map[s[r]] + 1
        hash_map[s[r]] = r
        max_len = max(max_len, r - l + 1)
        r += 1
    return max_len


if __name__ == "__main__":
    s = "abcba"
    print(longest_substrings(s))
    print(longest_substring_optimized(s))
