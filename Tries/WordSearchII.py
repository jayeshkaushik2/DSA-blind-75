from trie import TrieNode
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)

        rows, cols = len(board), len(board[0])
        res = set()
        visited = set()

        def dfs(i, j, node, wrd):
            if (
                (i < 0 or j < 0)
                or (i >= rows or j >= cols)
                or (board[i][j] not in node.children)
                or ((i, j) in visited)
            ):
                return None

            wrd += board[i][j]
            node = node.children[board[i][j]]
            visited.add((i, j))
            if node.is_word and wrd not in res:
                res.add(wrd)

            dfs(i, j + 1, node, wrd)
            dfs(i, j - 1, node, wrd)
            dfs(i + 1, j, node, wrd)
            dfs(i - 1, j, node, wrd)
            visited.remove((i, j))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")

        return list(res)


if __name__ == "__main__":
    # TODO have to fix
    cmds = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    words = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    print(f"Input: commands: {cmds}\nwords: {words}")
    sol = None
    res = []

    print(f"Output: {res}")
