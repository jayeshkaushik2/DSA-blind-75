from tree import TreeNode
from typing import Optional


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # TODO have to add the iterative approach

    # time comp O(N) and space comp O(1) where N = maximum number of nodes p and q
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == "__main__":
    # first testcase output should be True
    p1 = [1, 2, 3]
    q1 = [1, 2, 3]
    # second testcase output should be False
    # p1 = [1, 2]
    # q1 = [1, None, 2]
    print(f"Input: p -> {p1} and q -> {q1}")
    p_root = TreeNode()
    q_root = TreeNode()
    p_root.add_nodes(p1)
    q_root.add_nodes(q1)
    is_same_tree = isSameTree(p=p_root, q=q_root)
    print(f"Output: {is_same_tree}")
