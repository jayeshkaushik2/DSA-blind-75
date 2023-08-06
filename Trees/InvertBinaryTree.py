from Trees.tree import TreeNode


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None

    left = invertTree(root.left)
    right = invertTree(root.right)

    root.left = right
    root.right = left

    return root


if __name__ == "__main__":
    root = TreeNode()
    nodes_arr = [4, 2, 7, 1, 3, 6, 9]
    root.add_nodes(arr=nodes_arr)
    print("Input", f"root {nodes_arr}")
    # root.print_nodes(print_type="level_order")
    inverted_root = invertTree(root.next)
    print("Output")
    inverted_root.print_nodes(print_type="level_order")
