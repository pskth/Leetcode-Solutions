class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l = 0
        r = n - 1

        target = Counter(s1)
        freq = Counter(s2[l:r + 1])
        
        while r < len(s2):
            if target == freq:
                return True
            else:
                r += 1
                if r < len(s2):
                    freq[s2[r]] += 1
                freq[s2[l]] -= 1
                l += 1
        
        return False
