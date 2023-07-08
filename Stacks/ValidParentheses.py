def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    l = 0
    r = len(s)
    if r % 2 != 0:
        return False

    st = []

    while l < r:
        s_left = s[l]
        if s_left == "(" or s_left == "[" or s_left == "{":
            st.append(s_left)
        else:
            if not st:
                return False
            if (
                (s_left == ")" and st[-1] != "(")
                or (s_left == "]" and st[-1] != "[")
                or (s_left == "}" and st[-1] != "{")
            ):
                return False
            st.pop()

        l += 1
    if st:
        return False

    return True


if __name__ == "__main__":
    # s = "()"
    # s = ")"
    s = "((]))"
    print("Input:", s)
    res = isValid(s=s)
    print("Output:", res)
