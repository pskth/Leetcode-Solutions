class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
    '''
        Observation and spending quality time on the problem is key!
        By taking examples manually, we observe that multiplying by -1 is just passing around
        -ve sign to adjacent elements or destroying -ve if 2 -ve signs meet. Any 2 -ve signs
        even if they are far apart can be passed around and destroy.
        So, if number of negative elements is ODD:
            1 -ve sign will remain and it can be passed to the least abs(number).
        if number of negative elements is EVEN:
            all -ve signs will be destroyed

    '''
        minEle = float('inf')
        n = 0
        sumMatrix = 0
        for row in matrix:
            for ele in row:
                if ele < 0:
                    n += 1
                minEle = min(minEle, abs(ele))
                sumMatrix += abs(ele) 
        
        if n % 2:
            return sumMatrix - 2 * minEle
        else:
            return sumMatrix
