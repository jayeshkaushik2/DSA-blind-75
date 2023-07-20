import collections


def minWindow(s: str, t: str) -> str:
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
