from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # n = len(intervals)
        # res = []
        # i = 0
        # while i < n:
        #     cur = intervals[i]
        #     if cur[1] >= newInterval[0]:
        #         # merge the intervals
        #         if cur[1] > newInterval[1]:
        #             cur = cur
        #             i += 1
        #         else:
        #             cur = [cur[0], newInterval[1]]
        #             newInterval = cur
        #     res.append(cur)

        # return res

        # time comp O(N.log(N) + N) space comp O(N)
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        n = len(intervals)
        res = []

        for i in range(1, n):
            cur = intervals[i]

            if prev[1] < cur[0]:
                res.append(prev)
                prev = cur
            else:
                if prev[1] >= cur[1]:
                    prev = prev
                else:
                    prev = [prev[0], cur[1]]
        res.append(prev)

        return res


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(f"Inputs: \nintervals:{intervals}\nnewInterval:{newInterval}\n")
    output = sol.insert(intervals=intervals, newInterval=newInterval)
    print(f"Ouput: \n{output}")
