import collections
from tree import TreeNode


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # time comp O(N) space comp O(N) using inorder triversal
        stack = []
        cur_node = root
        i = 0

        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            node = stack.pop()
            if i + 1 == k:
                return node.val
            cur_node = node.right

        # time comp O(N.log(N) + N) space comp O(N)
        node_values = []
        que = collections.deque()
        que.append(root)

        while que:
            n = len(que)
            for i in range(n):
                node = que.popleft()
                node_values.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        node_values.sort()
        n = len(node_values)

        for i in range(n):
            if i + 1 == k:
                return node_values[i]


if __name__ == "__main__":
    solution = Solution()
    root_nodes = [3, 1, 4, None, 2]
    k = 1
    print("Input: ", root_nodes)
    root = TreeNode()
    root.add_nodes(arr=root_nodes)
    res_levels = solution.kthSmallest(root=root)
    print("Output: ", res_levels)
