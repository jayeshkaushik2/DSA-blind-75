from tree import TreeNode
from typing import Optional


def isEqualtree(tree1, tree2):
    if not tree1 and not tree2:
        return True

    if tree1 and tree2 and tree1.val == tree2.val:
        left_part = isEqualtree(tree1.left, tree2.left)
        right_part = isEqualtree(tree1.right, tree2.right)
        return left_part and right_part

    return False


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # TODO have to write the iterative approach

    # time comp O(N*N) [because we are checking if both root and subRoot are equal for email recursion call] space comp O(1)
    if not subRoot:
        return True
    if not root:
        return False

    if isEqualtree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


if __name__ == "__main__":
    # first testcase output should be True
    root_arr = [3, 4, 5, 1, 2]
    subRoot_arr = [4, 1, 2]
    # second testcase output should be False
    # root = [3,4,5,1,2,None,None,None,None,0]
    # subRoot = [4,1,2]
    print(f"Input: root -> {root_arr} and subRoot -> {subRoot_arr}")
    root = TreeNode()
    subRoot = TreeNode()
    root.add_nodes(root_arr)
    subRoot.add_nodes(subRoot_arr)
    is_sub_tree = isSubtree(root=root, subRoot=subRoot)
    print(f"Output: {is_sub_tree}")
