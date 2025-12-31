class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}

        def dp(r, c):
            if c < 0 or c >= n:
                return float('inf')
            if r == n - 1:
                return matrix[r][c]
…        return min(dp(0, c) for c in range(n))
