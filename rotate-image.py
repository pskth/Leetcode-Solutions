class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Observation:
        rotating image is equivalent to transpose + mirror matrix 
        via center vertical line of reference.

        Mostly got this idea beacuse I have solved it earlier and 
        in-place so must be something simple. like transpose or 
        mirroring.
        """

        n = len(matrix)

        # Transpose
        for j in range(n):
            for i in range(j):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Mirror across y - axis
        # Can use reverse() method on each row instead
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

        return None
