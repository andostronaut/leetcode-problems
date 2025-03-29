from typing import List


class Solution:
    def min_time_to_visit_all_points(self, points: List[List[int]]):
        res = 0

        x1, y1 = points.pop()

        while points:
            x2, y2 = points.pop()
            res += max(abs(y2 - y1), abs(x2 - x1))
            x1, y1 = x2, y2

        print(res)


sol = Solution()
sol.min_time_to_visit_all_points([[1, 1], [3, 4], [-1, 0]])
