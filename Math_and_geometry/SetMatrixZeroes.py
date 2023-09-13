from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        update_row = False

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        update_row = True

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        if update_row:
            for c in range(n):
                matrix[0][c] = 0


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(f"Input: matrix: {matrix}")
    sol.setZeroes(matrix=matrix)
    print(f"Output: {matrix}")
