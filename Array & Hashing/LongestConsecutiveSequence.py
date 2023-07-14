def longestConsecutive(nums: list[int]) -> int:
    temp = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in temp:
            # n is a start value
            cur = 0
            while (n + cur) in temp:
                cur += 1
            longest = max(longest, cur)

    return longest

    # brute force using sorting time comp O(N.log(N)) space comp O(1)
    nums.sort()
    n = len(nums)

    l = 0
    res = 0
    while l < n:
        prev = nums[l]
        l += 1
        cnt = 1
        while l < n:
            if nums[l] == prev:
                l += 1
            elif nums[l] == prev + 1:
                prev = nums[l]
                l += 1
                cnt += 1
            else:
                break
        res = max(res, cnt)

    return res


if __name__ == "__main__":
    # nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    # nums = [100,4,200,1,3,2]
    nums = [100, 4, 200, 1, 3, 2, 2, 2, 3, 3, 4, 4, 4, 3]
    print("Input:", nums)
    res = longestConsecutive(nums=nums)
    print("Output:", res)
