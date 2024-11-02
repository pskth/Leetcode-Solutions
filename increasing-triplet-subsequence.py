class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """Learn Longest Subsequence Algo's"""
        n1: int = 2*10**31+2
        n2: int = 2*10**31+2

        for n in nums:
            if n <= n1:
                n1 = n
            elif n <= n2:
                n2 = n
            else:
                return True
        return False
