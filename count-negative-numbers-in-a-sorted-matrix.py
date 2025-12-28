class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0

        for row in grid:
            l = 0
            h = len(row) - 1
            idx = -1

            while l <= h:
…            else:
                res += len(row) - idx

        return res
