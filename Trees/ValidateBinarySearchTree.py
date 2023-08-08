from typing import Optional
from tree import TreeNode


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # time comp O(N) space comp O(1)

        def validate(node, left, right):
            if not node:
                return True

            if node.val <= left or node.val >= right:
                return False

            return validate(node.left, left, node.val) and validate(
                node.right, node.val, right
            )

        return validate(root, float("-inf"), float("inf"))

        # does not complete all the edge cases
        que = [root]
        while que:
            cur_level_len = len(que)

            for i in range(cur_level_len):
                node = que.pop(0)
                if not node:
                    continue

                if node.left and node.right and node.left.val >= node.right.val:
                    return False
                if node.left and node.left.val >= node.val:
                    return False
                if node.right and node.right.val <= node.val:
                    return False

                que.append(node.left)
                que.append(node.right)

        return True


if __name__ == "__main__":
    solution = Solution()
    root_nodes = [1, 2, 3]
    # root_nodes = [1, 2, 3, None, 4, None, 0]
    # root_nodes = [5,4,6,null,null,3,7] # iterative approach fails this type of test cases
    print("Input: ", root_nodes)
    root = TreeNode()
    root.add_nodes(arr=root_nodes)
    is_valid_bts = solution.isValidBST(root=root)
    print("Output: ", is_valid_bts)
