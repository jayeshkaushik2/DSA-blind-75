from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        right[-1] = height[-1]

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        trapped_water = 0
        for i in range(n):
            trapped_water += min(left[i], right[i]) - height[i]

        return trapped_water


if __name__ == "__main__":
    sol = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Input: height: {height}")
    res = sol.trap(height=height)
    print(f"Output: res: {res}")
