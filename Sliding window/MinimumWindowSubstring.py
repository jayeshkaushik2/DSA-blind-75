import collections


def minWindow(s: str, t: str) -> str:
    # time comp O(N) space comp O(N + M)
    if t == "":
        return ""
    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    l = 0
    res = [-1, -1]
    resLen = float("inf")
    have, need = 0, len(countT)

    for r in range(len(s)):
        c = s[r]
        # Storing each ch from c to window
        window[c] = 1 + window.get(c, 0)
        # checking if c present in t and updating the have value by 1
        if c in countT and window[c] == countT[c]:
            have += 1

        # decrease the window size till have == need and update the resLen
        while have == need:
            if (r - l + 1) < resLen:
                resLen = r - l + 1
                res = [l, r]

            window[s[l]] -= 1

            # check if window[c] < countT[c] if does means we have to decrement the have by 1
            if s[l] in countT and countT[s[l]] > window[s[l]]:
                have -= 1
            l += 1

    l, r = res

    return s[l : r + 1] if resLen != float("inf") else ""

    def form_substring(ss):
        hm = collections.Counter(t)
        # when hm's values sum is equal to 0 thats when we know we found the sub string
        r = 0
        total_counts = sum(hm.values())

        while r < len(ss) and total_counts > 0:
            if hm.get(ss[r], 0) > 0:
                hm[ss[r]] -= 1
                total_counts -= 1

            if total_counts == 0:
                break
            r += 1

        return ss[: r + 1] if total_counts == 0 else ""

    res = ""
    first_update = True

    for l in range(len(s)):
        if s[l] in t:
            sub = form_substring(s[l:])
            if sub != "":
                if first_update:
                    res = sub
                    first_update = False
                if res != "" and len(res) > len(sub):
                    res = sub
            else:
                break

    return res


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print("Input:", f"s: {s}", f"t: {t}")
    res = minWindow(s=s, t=t)
    print("Output:", res)
