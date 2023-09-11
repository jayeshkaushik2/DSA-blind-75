from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # time comp O(N*N) space comp O(1)
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i, rows in enumerate(matrix):
            matrix[i] = rows[::-1]


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Input: matrix: {matrix}")
    sol.rotate(matrix=matrix)
    print(f"Output: {matrix}")
