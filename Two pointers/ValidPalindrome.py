def alpha_num(ch):
    ch_ord = ord(ch)
    if (
        ord("A") <= ch_ord <= ord("Z")
        or ord("a") <= ch_ord <= ord("z")
        or ord("0") <= ch_ord <= ord("9")
    ):
        return True
    return False


def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        # skip all none alpha numeric ch from left
        while l < r and not alpha_num(s[l]):
            l += 1
        # skip all none alpha numeric ch from right
        while l < r and not alpha_num(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1

    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    # s = "0P"
    print("Input:", s)
    res = isPalindrome(s=s)
    print("Output:", res)
