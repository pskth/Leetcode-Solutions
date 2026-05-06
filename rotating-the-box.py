class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        """
        Intital thought: in each row start from end have a 2 pointer type of approach
        Here: the 2 pointers are 1) [i][j] 2) free

        Start from the right end in each row, if its a obstacle, directly set free to j - 1
        if its a stone move it to free and set that position as empty.
        """
        m, n = len(boxGrid), len(boxGrid[0])
        free = n - 1
        
        for i in range(m):
            free = n - 1
            for j in range(n - 1 , -1 , -1):
                if boxGrid[i][j] == '*':
                    free = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][free] = '#'
                    free -= 1

        res = [['.' for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][i] = boxGrid[i][j]

        for row in res:
            row.reverse()

        return res
        
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
