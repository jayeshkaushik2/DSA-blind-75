from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            while i:
                count += i & 1
                i = i >> 1
            res.append(count)

        return res


if __name__ == "__main__":
    sol = Solution()
    n = 2
    print(f"Input: n: {n}")
    res = sol.countBits(n=n)
    print(f"Output res: {res}")
