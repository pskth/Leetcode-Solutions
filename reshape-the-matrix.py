class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        i, j = 0, 0 
        ans = [[0 for _ in range(c)] for _ in range(r)]
        for row in mat:
            for num in row:
                if j == c:
                    i += 1
                    j = 0
                ans[i][j] = num
                j += 1

        return ans