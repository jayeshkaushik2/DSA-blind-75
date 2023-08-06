from typing import Optional
from tree import TreeNode


def maxDepth(root: Optional[TreeNode]) -> int:
    # time comp O(N) space comp O(1)
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left + 1, right + 1)


if __name__ == "__main__":
    root = TreeNode()
    nodes_arr = root = [3, 9, 20, None, None, 15, 7]
    root.add_nodes(arr=nodes_arr)
    print("Input", f"root {nodes_arr}")
    # root.print_nodes(print_type="level_order")
    max_length = maxDepth(root.next)
    print("Output", max_length)
