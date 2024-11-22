class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    '''
        Forget making complete matrix as same value in each row, consider any 2 rows. How
        do we make 2 rows have same values? Is it possible for any 2 random rows?
        We observe that any all values of any 2 rows can be made same ONLY if they are equal
        or inverse of each other.
        We see that all rows can be put into groups where each row in a group is either equal
        or inverse. So there are only 2 type of members in a group.
        We count the length of each different group and return the max of it.

    '''
        count = {}
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            if matrix[row][0]:
                for col in range(n):
                    matrix[row][col] ^= 1

            count[tuple(matrix[row][:])] = count.setdefault(tuple(matrix[row][:]), 0) + 1

        return max(count.values())
