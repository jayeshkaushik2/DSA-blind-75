from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy approach time comp O(N) space comp O(1)
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

        n = len(nums)
        dp = {}

        # time comp O(N^N) space comp O(1) N = len(nums)
        # Unable to optimize with dp hashmap
        def dfs(i, dp):
            if i > len(nums) - 1:
                return True

            val = nums[i]
            if val == 0:
                if i < len(nums) - 1:
                    return False
                else:
                    return True

            for step in range(1, val + 1):
                if dfs(i + step, dp):
                    return True

            return False

        res = dfs(0, dp)
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 1, 4]
    print(f"Input: nums: {nums}")
    res = sol.canJump(nums=nums)
    print(f"Ouput: {res}")
