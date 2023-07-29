def lengthOfLongestSubstring(s: str) -> int:
    # time comp O(N) space comp O(N)
    r = 0
    subString = []
    longest_sub_string = 0

    while r < len(s):
        temp = s[r]
        while temp in subString:
            subString.pop(0)
        subString.append(temp)
        longest_sub_string = max(longest_sub_string, len(subString))
        r += 1

    return longest_sub_string


if __name__ == "__main__":
    s = "abcabcbb"
    print("Input:", s)
    res = lengthOfLongestSubstring(s=s)
    print("Output:", res)
