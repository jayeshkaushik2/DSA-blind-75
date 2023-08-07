from typing import Optional, List
from tree import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root is None:
            return []

        cur_level = [root]

        while cur_level:
            level_values = []
            cur_level_len = len(cur_level)

            for i in range(cur_level_len):
                node = cur_level.pop(0)
                level_values.append(node.val)

                if node.left:
                    cur_level.append(node.left)

                if node.right:
                    cur_level.append(node.right)

            if level_values:
                levels.append(level_values)

        return levels


if __name__ == "__main__":
    solution = Solution()
    root_nodes = [
        1,
        2,
        3,
        4,
        5,
        6,
        8,
        8,
        None,
        1,
        2,
        None,
        None,
        None,
        None,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]
    print("Input: ", root_nodes)
    root = TreeNode()
    root.add_nodes(arr=root_nodes)
    res_levels = solution.levelOrder(root=root)
    print("Output: ", res_levels)
