class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        ans = []
        for r in range(m):
            start = r * n
            end = start + n
            ans.append( original[start:end] )
        return ans
