from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])

        while left < right and top < bottom:
            # top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # last column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if top >= bottom or left >= right:
                break

            # bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # first col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Input: matrix: {matrix}")
    res = sol.spiralOrder(matrix=matrix)
    print(f"Output: {res}")
