import collections
from typing import List
from pprint import pprint


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                else:
                    if (
                        val in rows[r]
                        or val in cols[c]
                        or val in squares[(r // 3, c // 3)]
                    ):
                        return False
                    else:
                        rows[r].add(val)
                        cols[c].add(val)
                        squares[(r // 3, c // 3)].add(val)

        return True


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    print(f"Input: board: {pprint(board)}")
    res = sol.isValidSudoku(board=board)
    print(f"Output: res: {res}")
