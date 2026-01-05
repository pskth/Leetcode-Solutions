class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count, tot = 0, 0
        abs_min = math.inf
        zero_present = False
        
        for row in matrix:
            for num in row:
                tot += abs(num)
                abs_min = min(abs_min, abs(num))
                if num < 0:
                    neg_count += 1
                elif num == 0:
                    zero_present = True


        # print(f'{tot=}, {abs_min=}')
        if not zero_present and neg_count > 0 and neg_count % 2:
            return tot - 2*abs_min
        else:
            return tot
         