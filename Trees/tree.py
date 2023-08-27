class Tree:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class TreeNode:
    def __init__(self):
        root = None

    def add_nodes(self, arr, add_type="recursive"):
        if add_type == "itervative":
            pass
        elif add_type == "recursive":
            if not arr:
                return None
            self.i = 0

            def dfs():
                print(arr, self.i)
                if self.i >= len(arr) or arr[self.i] == None:
                    self.i += 1
                    return None

                root = Tree(arr[self.i])
                self.i += 1
                root.left = dfs()
                root.right = dfs()
                return root

            self.root = dfs()

    def print_nodes(self, print_type="pre_order"):
        if print_type not in ("level_order", "pre_order", "post_order", "in_order"):
            print(
                "Invalid print type, print_type should be from: ",
                ("level_order", "pre_order", "post_order", "in_order"),
            )
            return

        def dfs(cur_node):
            if not cur_node:
                print("None", end="->")
                return

            print(cur_node.val, end="->")
            dfs(cur_node=cur_node.left)
            dfs(cur_node=cur_node.right)

        return dfs(self)
