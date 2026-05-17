from collections import Counter


def check_anagrams(s, t):
    len_s = len(s)
    len_t = len(t)

    if len_s == 0 or len_t == 0:
        return 0

    if len_t > len_s:
        return 0

    ana_count = 0

    l = 0
    r = 0

    exp_freq, win_freq = [0] * 26, [0] * 26

    for c in t:
        exp_freq[ord(c) - ord("a")] += 1

    # expand window till size of t is met
    while r < len_s:
        win_freq[ord(s[r]) - ord("a")] += 1
        if r - l + 1 == len_t:
            if win_freq == exp_freq:
                ana_count += 1
            win_freq[ord(s[l]) - ord("a")] -= 1
            l += 1
        r += 1

    return ana_count


if __name__ == "__main__":
    s = "caabab"
    t = "aba"

    print(check_anagrams(s, t))
