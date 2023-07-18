def characterReplacement(s: str, k: int) -> int:
    max_length = 0
    l = 0
    counts = {}
    for r in range(len(s)):
        counts[s[r]] = 1 + counts.get(s[r], 0)

        print(counts)
        # removing all the left most elements from the counts till window_size - max_frequency <= k
        while (r - l + 1) - max(counts.values()) > k:
            counts[s[l]] -= 1
            l += 1

        max_length = max(max_length, r - l + 1)

    return max_length


if __name__ == "__main__":
    s = "ABABBA"
    k = 2
    print("Input:", f"s: {s}", f"k: {k}")
    res = characterReplacement(s=s, k=k)
    print("Output:", res)
