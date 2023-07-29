def containsDuplicate(nums: list[int]) -> bool:
    # using hashmap
    # hm = {}
    # for n in nums:
    #     if n in hm:
    #         return True
    #     hm[n] = 1

    # return False

    # using set
    hset = set(nums)
    return len(hset) != len(nums)


if __name__ == "__main__":
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print("Input:", nums)
    res = containsDuplicate(nums=nums)
    print("Output:", res)
