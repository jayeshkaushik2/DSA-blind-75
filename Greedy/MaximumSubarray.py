from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # time comp O(N) space comp O(1)
        cur_sum = max_sum = nums[0]
        for n in nums[1:]:
            if cur_sum >= 0:
                cur_sum += n
            else:
                cur_sum = n
            max_sum = max(max_sum, cur_sum)

        return max_sum

        # brute force solution time comp O(N) space comp O(1)
        n = len(nums)
        res = float("-inf")

        for i in range(n):
            temp = nums[i]
            for j in range(i + 1, n):
                temp += nums[j]
                res = max(res, temp)
            res = max(res, temp)

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: nums: {nums}")
    res = sol.maxSubArray(nums=nums)
    print(f"Ouput: {res}")
