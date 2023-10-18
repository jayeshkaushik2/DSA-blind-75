from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r -= 1
            else:
                l += 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(f"Input nums: {nums} target:{target}")
    res = sol.search(nums=nums, target=target)
    print(f"Output: {res}")
