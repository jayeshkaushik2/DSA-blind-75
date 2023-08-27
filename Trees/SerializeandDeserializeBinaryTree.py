from tree import TreeNode


class Solution:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        arr = []

        def dfs(cur_node):
            if not cur_node:
                arr.append("N")
                return
            arr.append(str(cur_node.val))
            dfs(cur_node.left)
            dfs(cur_node.right)

        dfs(root)
        return ",".join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        self.i = 0

        def dfs():
            if arr[self.i] == "N":
                self.i += 1
                return None

            root = TreeNode(arr[self.i])
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        root = dfs()
        return root


if __name__ == "__main__":
    sol = Solution()
    root_nodes = [1, 2, 3, None, None, 4, 5]
    print("Input: ", f"root: {root_nodes}")

    root = TreeNode()
    root.add_nodes(arr=root_nodes)

    # encoded root string
    encoded_data = sol.serialize(root)
    print("Output: ")
    print("Encoded string: ", encoded_data)
    # root decoded
    decoded_data = sol.deserialize(data=encoded_data)
    print("Decoded Tree: ", decoded_data.print_nodes())
