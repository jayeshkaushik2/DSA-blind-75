from typing import Optional
from tree import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root) -> tuple:
            """returns a tuple -> (whether the root is balanced, height of the root)"""
            if not root:
                return True, 0

            left = dfs(root.left)
            right = dfs(root.right)
            # check if root is balanced -> when the left and right is balanced and there height difference is <= 1
            is_balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

            return is_balanced, 1 + max(left[1], right[1])

        return dfs(root)[0]


if __name__ == "__main__":
    sol = Solution()
    root_nodes = [3, 9, 20, None, None, 15, 7]
    print("Input: ", root_nodes)
    root = TreeNode()
    root.add_nodes(arr=root_nodes)
    breakpoint()
    res = sol.isBalanced(root=root.root)
    print("Output: ", res)
