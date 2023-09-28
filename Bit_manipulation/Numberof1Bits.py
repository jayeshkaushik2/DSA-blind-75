class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n = n >> 1

        return res


if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(f"Input: n:{n}")
    res = sol.hammingWeight(n=n)
    print(f"Output: res:{res}")
