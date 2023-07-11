List = list


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # time comp O(N^2 * 100.log(100)) space comp O(N) + O(N)
    res = []
    n = len(strs)
    marked = [False] * n

    def is_anagram(a1, a2):
        return sorted(a1) == sorted(a2)

    for i in range(n):
        if not marked[i]:
            temp = [strs[i]]
            marked[i] = True
            for j in range(i + 1, n):
                if not marked[j] and is_anagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    marked[j] = True
            res.append(temp)

    return res


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Input:", strs)
    res = groupAnagrams(strs=strs)
    print("Output:", res)
