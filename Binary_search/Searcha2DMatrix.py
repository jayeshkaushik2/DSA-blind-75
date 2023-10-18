from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)

        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            else:
                r = len(matrix[i])
                while l < r:
                    mid = (l + r) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        r -= 1
                    else:
                        l += 1

        return False


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(f"Input matrix: {matrix} target:{target}")
    res = sol.searchMatrix(matrix=matrix, target=target)
    print(f"Output: {res}")
