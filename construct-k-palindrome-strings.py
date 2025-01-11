class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        
        count = collections.Counter(s)
        noOfOdds = 0

        for c in count.values():
            if c & 1:
                noOfOdds += 1
        
        if noOfOdds > k:
            return False
        else:
            return True
