s = "aacb"
k = 1

# aaa


def longest_uniform_substring(s, k):

    # Keep pointers at the start of the string
    left = right = 0
    freqs = {}
    highest_freq = 0
    max_len = 0

    while right < len(s):

        print(s[left : right + 1])

        # find highest character frequency in the current window
        # Keep right pointer as base and go char by char
        freqs[s[right]] = freqs.get(s[right], 0) + 1
        highest_freq = max(freqs[s[right]], highest_freq)

        # num of chracters to replace
        num_char_to_replace = (right - left + 1) - highest_freq

        if num_char_to_replace > k:
            freqs[s[left]] -= 1
            left += 1
        max_len = right - left + 1
        right += 1

    return max_len


if __name__ == "__main__":
    print(longest_uniform_substring(s, k))
