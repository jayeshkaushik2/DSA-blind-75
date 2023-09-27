from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(i, values, cur_sum):
            if cur_sum == target:
                res.append(values.copy())
                return
            elif i < 0 or i == n or cur_sum > target:
                return

            values.append(candidates[i])
            dfs(i, values, cur_sum + candidates[i])
            values.pop()
            dfs(i + 1, values, cur_sum)

        dfs(0, [], 0)

        return res


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(f"Input: candidates:{candidates}, target:{target}")
    sol = Solution()
    res = sol.combinationSum(candidates=candidates, target=target)
    print(f"Output: res:{res}")
