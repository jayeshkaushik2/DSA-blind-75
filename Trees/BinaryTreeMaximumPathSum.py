from tree import TreeNode
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]

        def dfs(root):
            if not root:
                return 0

            cur_sum = root.val
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            res[0] = max(res[0], left + right + cur_sum)

            return max(left, right) + cur_sum

        dfs(root)

        return res[0]


if __name__ == "__main__":
    solution = Solution()
    root_nodes = [1, 2, 3]
    # root_nodes = [-8]
    print("Input: ", f"root: {root_nodes}")
    root = TreeNode()
    root.add_nodes(arr=root_nodes)
    max_path_sum = solution.maxPathSum(root=root)
    print("Output: ", max_path_sum)
