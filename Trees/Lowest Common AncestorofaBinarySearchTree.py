from tree import TreeNode


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    cur_node = root

    while cur_node:
        if p.val > cur_node.val and q.val > cur_node.val:
            cur_node = cur_node.right
        elif p.val < cur_node.val and q.val < cur_node.val:
            cur_node = cur_node.left
        else:
            return cur_node


if __name__ == "__main__":
    root_nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 2
    q = 8
    root = TreeNode()
    root.add_nodes(arr=root_nodes)
    print("Input", f"root {root_nodes}")
    # root.print_nodes(print_type="level_order")
    res_root = lowestCommonAncestor(root.next)
    print("Output", res_root.val)
