List = list


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # time comp O(N.log(N) + O(k)) space comp O(N)
    hm = {}
    res = []

    for n in nums:
        hm[n] = hm.get(n, 0) + 1

    hm = {key: val for key, val in sorted(hm.items(), key=lambda x: x[1], reverse=True)}
    i = 0
    while i < len(nums) and i < k:
        res.append(list(hm.items())[i][0])
        i += 1

    return res


if __name__ == "__main__":
    # nums, k = [1, 1, 1, 2, 2, 3], 2
    nums, k = [1, 2], 2

    print("Input:", "nums: {nums}", f"k: {k}")
    res = topKFrequent(nums=nums, k=k)
    print("Output:", res)
