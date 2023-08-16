from tree import TreeNode
from typing import Optional


class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root


if __name__ == "__main__":
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print("Input: ", f"preorder: {preorder}, inorder: {inorder}")
    binary_tree = solution.buildTree(preorder=preorder, inorder=inorder)
    print("Output: ", binary_tree)
