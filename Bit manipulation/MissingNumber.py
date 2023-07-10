def missingNumber(nums: list[int]) -> int:
    # second solution slightly better approach with same time and space comp
    res = len(nums)
    for i in range(len(nums)):
        res += i - nums[i]
    return res

    # first solution with time comp O(N) space comp O(1)
    total_sum = sum(range(0, len(nums) + 1))
    cur_sum = sum(nums)
    return abs(total_sum - cur_sum)


if __name__ == "__main__":
    nums = [3, 0, 1]
    print("Input:", nums)
    res = missingNumber(nums=nums)
    print("Output:", res)
