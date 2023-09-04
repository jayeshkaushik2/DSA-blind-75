from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        n = len(intervals)
        res = []

        for i in range(1, len(intervals)):
            cur = intervals[i]
            if prev[1] < cur[0]:
                res.append(prev)
                prev = cur
            else:
                if prev[1] > cur[1]:
                    prev = prev
                else:
                    prev = [prev[0], cur[1]]

        res.append(prev)
        return res


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Inputs: \nintervals:{intervals}")
    output = sol.merge(intervals=intervals)
    print(f"Ouput: \n{output}")
