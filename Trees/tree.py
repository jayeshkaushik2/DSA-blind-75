class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def add_nodes(self, arr, add_type="itervative"):
        arr = [4, 2, 7, 1, 3, 6, 9]

        if add_type == "itervative":
            pass
        elif add_type == "recursive":
            left = self.add_nodes()

    def print_nodes(self, print_type):
        if print_type not in ("level_order", "pre_order", "post_order", "in_order"):
            print(
                "Invalid print type, print_type should be from: ",
                ("level_order", "pre_order", "post_order", "in_order"),
            )
            return
