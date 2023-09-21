from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time comp O(M*N*len_of_word) space comp O(N)

        m, n = len(board) - 1, len(board[0]) - 1
        visited = set()

        def dfs(r, c, i):
            if i > len(word) - 1:
                return True

            if (
                r > m
                or c > n
                or r < 0
                or c < 0
                or (r, c) in visited
                or word[i] != board[r][c]
            ):
                return False

            i += 1
            visited.add((r, c))
            res = (
                dfs(r + 1, c, i)
                or dfs(r - 1, c, i)
                or dfs(r, c + 1, i)
                or dfs(r, c - 1, i)
            )
            visited.remove((r, c))
            return res

        for r in range(m + 1):
            for c in range(n + 1):
                if dfs(r, c, 0):
                    return True

        return False


if __name__ == "__main__":
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(f"Input: board: {board} word: {word}")
    res = sol.exist(board=board, word=word)
    print(f"Ouput: {res}")
