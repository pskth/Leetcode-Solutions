class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0]*32

        for n in candidates:
            i = 0
            while n > 0:
                count[i] += n & 1
                i += 1
                n = n >> 1
        return max(count)
