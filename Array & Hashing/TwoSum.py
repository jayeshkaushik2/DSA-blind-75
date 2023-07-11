def twoSum(nums: list[int], target: int) -> list[int]:
    # using hashmap time comp O(N) space comp O(N)
    hm = {}
    for i, ele in enumerate(nums):
        if target - ele in hm:
            return [hm[target - ele], i]
        hm[ele] = i

    # brute force solution time comp O(N^2) space comp O(1)
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    return [-1, -1]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Input:", f"nums: {nums}", f"target: {target}")
    res = twoSum(nums=nums, target=target)
    print("Output:", res)
