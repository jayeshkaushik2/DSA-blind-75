from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum == target:
                return [l + 1, r + 1]
            elif cur_sum > target:
                r -= 1
            else:
                l += 1


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 10, 15]
    target = 9
    print(f"Input: nums: {nums}, target:{target}")
    res = sol.twoSum(numbers=nums, target=target)
    print("Output:", res)
