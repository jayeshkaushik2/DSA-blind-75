class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev1 = 1
        prev2 = 2
        for i in range(3, n + 1):
            temp = prev1 + prev2
            prev1 = prev2
            prev2 = temp

        return prev2

        # recursive approach time comp O(N) space comp O(1)
        store = {1: 1, 2: 2, 3: 3}

        def dfs(n, store):
            if n < 0:
                return 1

            if n in store:
                return store[n]

            p1 = self.climbStairs(n - 1)
            store[n - 1] = p1
            p2 = self.climbStairs(n - 2)
            store[n - 2] = p2

            return p1 + p2

        return dfs(n, store)


if __name__ == "__main__":
    sol = Solution()
    n = 43
    print(f"Input n:{n}")
    steps = sol.climbStairs(n)
    print(f"Output Steps:{steps}")
