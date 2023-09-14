from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

        # time comp O(N) space O(1)
        for i, n in enumerate(nums):
            if n == target:
                return i

        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(f"Input nums: {nums} target:{target}")
    res = sol.search(nums=nums, target=target)
    print(f"Output: {res}")
