class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
    '''
        Simulation:
        To rotate the box, take the transpose but row should inserted from the end.
        Maintain 2 Pointers top, bottom. If top encouters a stone place it at bottom.
        Else if top encounters an obstacle, bring bottom pointer to top - 1.

    '''
        m = len(box)
        n = len(box[0])
        ans = [["."] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ans[j][m - i - 1] = box[i][j]

        for col in range(m):
            top, bottom = n - 1, n - 1
            while top >= 0:
                if ans[top][col] == "#":
                    ans[top][col] = "."
                    ans[bottom][col] = "#"
                    bottom -= 1
                if ans[top][col] == "*":
                    bottom = top - 1
                top -= 1
        return ans
