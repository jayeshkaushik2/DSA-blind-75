import collections


def isAnagram(s: str, t: str) -> bool:
    # time comp O(N) space comp O(2N)
    s_hm = collections.Counter(s)
    t_hm = collections.Counter(t)

    for key in t_hm:
        if t_hm[key] != s_hm.get(key, 0):
            return False

    for key in s_hm:
        if s_hm[key] != t_hm.get(key, 0):
            return False

    return True

    # second approach is to sort them and compare to each other
    # time comp O(N.log(N)) space comp O(1)
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    # s, t = "anagram", "nagaram"
    # s, t = "rat", "car"
    s, t = "ab", "b"
    print("Input:", f"s: {s}", f"t: {t}")
    res = isAnagram(s=s, t=t)
    print("Output:", res)
