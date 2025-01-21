class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = sum(grid[0][:]) - grid[0][0]
        bottom = 0
        ans = top

        for i in range(1, n):
            top -= grid[0][i]
            bottom += grid[1][i - 1]
            ans = min(ans, max(top, bottom))
        
        return ans
